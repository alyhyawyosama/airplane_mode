// Copyright (c) 2024, OSAma and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airplane Ticket", {
	refresh: function(frm) {
        // To show only the unique elements 
        // First way 
        frm.set_query('item', 'add_ons', function(doc, cdt, cdn) {
            var used_items = [];

            $.each(doc.add_ons, function(idx, val){
                // Check the if the added row has already value then push it                 
                if (val.item) 
                    used_items.push(val.item);
			});
            return {
                // Get the parent doctype and the name field then check the values that are not in used_items 
                filters: [
                    ['Airplane Ticket Add-on Type', 'name', 'not in', used_items]
                ]
            }
        });
        // Second way 
        // frm.fields_dict['add_ons'].grid.get_field('item').get_query = function(doc, cdt, cdn) {
        //     let d = locals[cdt][cdn];
        //     var used_items = [];

        //     // $.each(doc.add_ons, function(idx, val){
        //     //     // Check the if the added row has already value then push it                 
        //     //     if (val.item) 
        //     //         used_items.push(val.item);
		// 	// });
        //     // return {
        //     //     // Get the parent doctype and the name field then check the values that are not in used_items 
        //     //     filters: [
        //     //         ['Airplane Ticket Add-on Type', 'name', 'not in', used_items]
        //     //     ]
        //     // }
        // };
        
    },    

    flight_price:function(frm) {
        frm.trigger("refresh_total_amount")
    },

    refresh_total_amount(frm){
        var total = frm.doc.flight_price
        // Calculte to total amount of elements in the child table 
        $.each(cur_frm.doc.add_ons, function(idx, val){
            if(val.item) total += val.amount 
        });


        frm.set_value("total_amount", total);
        frm.refresh_field("total_amount");
       
    },
});



frappe.ui.form.on("Airplane Ticket Add-on Item", {
    amount:function (frm,cdt,cdn) {
        frm.trigger("refresh_total_amount")
    },

    add_ons_add:function (frm,cdt,cdn) {
        frm.trigger("refresh_total_amount")
    },

    add_ons_remove:function (frm,cdt,cdn) {
        frm.trigger("refresh_total_amount")
    }

    



})

