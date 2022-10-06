// Copyright (c) 2022, MUHAMMED and contributors
// For license information, please see license.txt

frappe.ui.form.on('Client Side doctype', {
// 	after_save : function ( frm ) {
// 		frappe.msgprint( __("The full name is '{0}'",
// 		        [frm.doc.first_name+ " " + frm.doc.middle_name + " " + frm.doc.last_name]))
		
// 	    for (let row of frm.doc.family_member) {
// 		    frappe.msgprint(__("{0}. The family member name is '{1}' and relation is '{2}'",
// 			[row.idx,row.name1,row.relation]))
// 	}
// }
// refresh : function ( frm ) {
// //     frm.set_intro ( ' Now you can ctreate a new Client Side Scripting doctype ' )
// // }
// if (frm.is_new ()) {
//     frm.set_intro ( ' Now you can ctreate a new Client Side Scripting doctype ' )
// }
//        }       
// validate : function ( frm ) {
//     // frm.set_value ('full_name', frm.doc.first_name +"  "+frm.doc.middle_name +"  "+ frm.doc.last_name)
//     let row = frm.add_child('family_member',{
//         name1:'johnson jose',
//         relation:'Father',
//         age:56,
//     })

// }
// enable:function(frm){
//     // frm.set_df_property('first_name','reqd',1)
//     // frm.set_df_property('middle_name','read_only',1)
//     frm.toggle_reqd('age', true)

refresh:function(frm) {
//     frm.add_custom_button('Click Me Button',()=>{
//     frappe.msgprint(__('You Clicked Me!!'));
    
//     })
frm.add_custom_button('Click Me1',()=>{

    frappe.msgprint(('You Clicked 1!!'));
},'click me')
frm.add_custom_button('Click Me2',()=>{

    frappe.msgprint(('You Clicked 2!!'));
},'click me')






}


    
    
    
    
    



    });
	
	
		

