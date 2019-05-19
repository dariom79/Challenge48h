#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 18 11:29:49 2019

@author: Dario Mastroeni
"""

import scrapy
from dario_challenge.items import TreeItem


class Challenge48h(scrapy.Spider):
    name = "DecisionTree"
    
    
    def start_requests(self):
        url = 'https://www.drukzo.nl.joao.hlop.nl/python.php'
        yield scrapy.Request(url=url, callback=self.parse, meta={"parent": "-",
                                                                 "prev_drop": "-"})
    

    def parse(self, response):
        parent = response.meta['parent']
        prev_drop = response.meta['prev_drop']
        current_drop = response.xpath("//select")[-1].attrib["id"]
        if current_drop != prev_drop:
            self.log("Parent: -> " + parent)
            opt_list = response.xpath("//select[@id='"+ current_drop +"']/option/text()")
            for opt in opt_list:
                val = opt.extract()
                self.log(val)
                yield scrapy.FormRequest.from_response(response, 
                                                       formdata = {current_drop: val},
                                                       callback=self.parse,
                                                       meta={"parent": val,
                                                             "prev_drop": current_drop})
                new_item = TreeItem()
                new_item['parent'] = parent
                new_item['element'] = val
                yield new_item
      