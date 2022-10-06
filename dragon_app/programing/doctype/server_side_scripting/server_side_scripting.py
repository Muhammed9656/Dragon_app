# Copyright (c) 2022, MUHAMMED and contributors
# For license information, please see license.txt



from dataclasses import fields
import frappe
from frappe import _
from frappe.model.document import Document

class Serversidescripting (Document) :
    pass
    # def validate(self): 
    #   frappe.msgprint("hello")
    # def before_save(self):
    #     frappe.throw("hello frappe from before_save event")
    # def before_insert(self):
    #     frappe.throw("hello frappe from before_insert event")
    # def after_insert(self):
    #     frappe.throw("hello frappe from after_insert event")
    # def on_update(self):
    #     frappe.msgprint("hello frappe from 'on_update' event")
    # def before_submit(self):
    #     frappe.msgprint("hello frappe from 'before_submit'event")
    # def on_submit(self):
    #     frappe.msgprint("hello frappe from 'on_submit'event")
    # def on_cancel(self):
    #     frappe.msgprint("hello frappe from 'on_cancel',event")
    # def on_trash(self):
    #     frappe.msgprint("hello frappe from 'on_trash'event")
    # def after_delete(self):
    #     frappe.msgprint("hello 'after_delete'event")
    
    ########################## value fetching#################
    # def validate(self):
    #     frappe.msgprint(_("hello my full name is '{0}' ").format(self.first_name+" "+self.middle_name+" "+self.last_name))
    # def validate(self):
    #     for row in  self.get("family_member"):
    #         frappe.msgprint(_("{0} The family member name is '{1}'and relation is '{2}'").format(row.idx,row.name1,row.relation))
    # def validate(self):
    #     self.get_document()
        
    # def get_document(self):  
    #     doc = frappe.get_doc('Client Side doctype',self.client_side_doc) 
    #     frappe.msgprint(_("The First Name is '{0}' And  Age is {1}").format(doc.first_name,doc.age))
        
    
    #     for row in doc.get("family_member"):
    #          frappe.msgprint((
    #          "{0}. The family member name is '{1}'  and relation is '{2}'").format(row.idx,row.name1,row.relation))
    
            ######################### #frappe.new_doc(doctype)################################

             
             
    # def validate(self):
    #     self.new_document()
    # def new_document(self):
    #     doc=frappe.new_doc("Client Side doctype")
    #     doc.first_name="MUHAMMED"
    #     doc.last_name="ibnu arif n p"
    #     doc.age=65
    #     doc.append("family_member",{ "name1":"Naaa",
                                
    #                                   "relation":"frnd",
    #                                   "age":85
                                    
            
    #     })
        
    #     doc.insert()
        
        ############frapee.delete_doc(doxtype,name)########################
        
        # def validate(self):
        #     frappe.delete_doc("Client Side doctype","PR-00011")
        
        
        ############### DOCUMENT METHODS####################
    # def validate(self):
    #     self.save_document()
    # def save_document(self):
    #     doc=frappe.new_doc("Client Side doctype")
    #     doc.first_name="MUHA"
    #     doc.last_name="ibnu arif n p"
    #     doc.age=65
    #     doc.save()
    
    
    #doc_delete()
    
    # def validate(self):
    #     self.delete_document()
    # def delete_document():
    #     doc=frappe.get_doc("Client Side doctype","PR-00004")
    
    #################doc.db_set()###################
    
    # def validate(self):
    #     self.db_set_document()
    # def db_set_document(self):
    #     doc=frappe.get_doc("Client Side doctype","PR-00003")
    #     doc.db_set('age',85)
    
    #view all enalbed
    
    # def validate(self):
    #     self.get_list()
        
    # def get_list(self):
    #     doc = frappe.db.get_list("Client Side doctype",
    #             filters={
    #                 'enable': 1
    #             },
    #             fields=['first_name','age']
    #             )
    #     for d in doc:
    #         frappe.msgprint(_("THe parent name is {0} and age is {1}").format(d.first_name,d.age))
    
    ###############frappe.db.ge_value()######################33
    
    
    # def validate(self):
    #     self.get_value()
    # def get_value(self):
        
    #     first_name,age=frappe.db.get_value("Client Side doctype","PR-00017",["first_name",'age'])
    #     frappe.msgprint(("The Parent first name is {0} and age is {1}").format(first_name,age))
    
    ############frappe.db.set_value()##########################
    
    
    # def validate(self):
    #     self.set_value()
        
    # def set_value(self):
    #     frappe.db.set_value("Client Side doctype","PR-00017","age",25)
    #     first_name,age=frappe.db.get_value("Client Side doctype","PR-00017",["first_name",'age'])
    #     frappe.msgprint(("The Parent first name is {0} and age is {1}").format(first_name,age))
    
    #######################  FRAPPE.DB.EXISTS(DOCTYPE,NAME)#######################
    
    
    # def validate(self):
    #     if frappe.db.exists("Client Side doctype ",'PR-00019'):
    #         frappe.msgprint("THE DOCUMENT IS EXISTS IN DATABASE")
    #     else:
    #         frappe.msgprint("THE DOCUMENT IS NOT EXISTS IN DATABASE")
        
        ##################frappe.db.count()#####################
        
        # def validate (self):
        #     doc_count=frappe.db.count('Client Side doctype', {'enable':1})
        #     frappe.msgprint(('The Enable Document Count is {0}').format(doc_count))
                                                              
                                                             
       ############ frappe.db.sql##############3
       
    #    def validate(self):
    #        self.sql()
           
    #    def sql(self):
           
    #        data = frappe.db.sql("""
    #                                SELECT
    #                                   first_name,
    #                                    age
    #                                FROM
    #                                    `tabClient Side doctype`
    #                                WHERE
    #                                     enable=1
    #                         """,    as_dict=1)
    #        for d in data:
    #            frappe.msgprint(("The Parent First Name is {0} and age is {1}").format(d.first_name,d.age))
        #  @frappe.whitelist()
        #  def frm_call(self,msg):
        #      import time
        #      time.sleep(5)
        #     #  frappe.msgprint(msg)
             
        #      self.mobile = 965681643
             
            #  return "Hi This message from frm_call"
                                
       
       
                  
    
    
    
