// Copyright (c) 2022, MUHAMMED and contributors
// For license information, please see license.txt

frappe.ui.form.on('Server side scripting', {
	// refresh: function(frm) {

	// }
	enable:function(frm){
	   frappe.call({
		   method:'dragon_app.programing.doctype.client_side_doctype.client_side_doctype.frappe_call',
		   args:{
			   msg:"Hello"
			
			
		   },
		   freeze:true,
		   freeze_message: __('Calling frappe_call Method'),
		   callback: function(r){
			   frappe.msgprint(r.message)
		   }

		

	   });
	}
});
