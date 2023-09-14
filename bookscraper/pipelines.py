import scrapy
from itemadapter import ItemAdapter


class BookscraperPipeline(object):
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        
        # Iterate through all fields of the item and strip whitespaces
        for field_name in adapter.field_names():
            if field_name!='description':
                field_value = adapter.get(field_name)
                # Strip whitespaces from the string field
                adapter[field_name] = field_value.strip()



        lower_keys =['category', 'product_type']
        for lower_key in lower_keys:
            value =adapter.get(lower_key)
            adapter[lower_key] = value.lower()


        price_keys =['price','price_excl_tax','price_incl_tax']
        for price_key in price_keys:
            value = adapter.get(price_key)
            value= value.replace('$','')
            adapter[price_key]=float(value)



        nmb_reviews = adapter.get('nmb_reviews')
        adapter['nmb_reviews']=int(nmb_reviews)



        stars_text = adapter.get('stars')
        splice_stars_array = stars_text.split(' ')
        stars_text_value = splice_stars_array[1].lower()

        if stars_text_value =='zero':
            adapter['stars']=0
        if stars_text_value =='one':
            adapter['stars']=1

        if stars_text_value =='two':
            adapter['stars']=2
        
        if stars_text_value =='three':
            adapter['stars']=3
        
        if stars_text_value =='four':
            adapter['stars']=4
        
        if stars_text_value =='five':
            adapter['stars']=5
        
        return item
