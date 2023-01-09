/* =====================================
All JavaScript fuctions Start
======================================*/
(function ($) {
	
    'use strict';
/*--------------------------------------------------------------------------------------------
	document.ready ALL FUNCTION START
---------------------------------------------------------------------------------------------*/	

//  selectpicker function by = bootstrap-select.min.js ========================== //
	function select_picker_select(){
		jQuery('.my-select').selectpicker();
	}

//  Home 1 Banner Carousel function by = owl.carousel.js ========================== //
	function twm_h1_bnr_carousal(){
		jQuery('.twm-h1-bnr-carousal').owlCarousel({
			animateIn: 'fadeIn',
			animateOut: 'fadeOut',
			items: 1,
			loop: true,
			nav:false,
			dots: false,
			autoplay:true,
			autoplayHoverPause:false,
			touchDrag  : false,
			mouseDrag  : false,
		});
	}

//  Job Categories Carousel function by = owl.carousel.js ========================== //
	function job_categories_carousel(){
		jQuery('.job-categories-carousel').owlCarousel({
			loop:true,
			nav:true,
			dots: false,
			center:false,				
			margin:30,
			autoplay:true,
			navText: ['<i class="feather-chevron-left"></i>', '<i class="feather-chevron-right"></i>'],
			responsive:{
				0:{
					items:1,
				},
				480:{
					items:1,
				},			
				767:{
					items:2,
					margin:0,
				},
				991:{
					items:2,
					
				},
				1024:{
					items:3
				}
			}
		});
	}

// > Video responsive function by = custom.js ========================= //	
	function video_responsive(){	
		jQuery('iframe[src*="youtube.com"]').wrap('<div class="embed-responsive embed-responsive-16by9"></div>');
		jQuery('iframe[src*="vimeo.com"]').wrap('<div class="embed-responsive embed-responsive-16by9"></div>');	
	}  

// > LIGHTBOX Gallery Popup function	by = lc_lightbox.lite.js =========================== //      
 	function lightbox_popup(){
        lc_lightbox('.elem', {
            wrap_class: 'lcl_fade_oc',
            gallery : true,	
            thumb_attr: 'data-lcl-thumb', 
            
            skin: 'minimal',
            radius: 0,
            padding	: 0,
            border_w: 0,
        });
	}			

// > magnificPopup for video function	by = magnific-popup.js ===================== //	
	function magnific_video(){	
		jQuery('.mfp-video').magnificPopup({
			type: 'iframe',
		});
	}

// Vertically center Bootstrap modal popup function by = custom.js ==============//
	function popup_vertical_center(){	
		jQuery(function() {
			function reposition() {
				var modal = jQuery(this),
				dialog = modal.find('.modal-dialog');
				modal.css('display', 'block');
				
				// Dividing by two centers the modal exactly, but dividing by three 
				// or four works better for larger screens.
				dialog.css("margin-top", Math.max(0, (jQuery(window).height() - dialog.height()) / 2));
			}
			// Reposition when a modal is shown
			jQuery('.modal').on('show.bs.modal', reposition);
			// Reposition when the window is resized
			jQuery(window).on('resize', function() {
				jQuery('.modal:visible').each(reposition);
			});
		});
	}

// > Main menu sticky on top  when scroll down function by = custom.js ========== //		
	function sticky_header(){
		if(jQuery('.sticky-header').length){
			var sticky = new Waypoint.Sticky({
			  element: jQuery('.sticky-header')
			});
		}
	}

// > Sidebar sticky  when scroll down function by = theia-sticky-sidebar.js ========== //		
	function sticky_sidebar(){		
		$('.rightSidebar')
			.theiaStickySidebar({
				additionalMarginTop: 100
			});		
	}

// > page scroll top on button click function by = custom.js ===================== //	
	function scroll_top(){
		jQuery("button.scroltop").on('click', function() {
			jQuery("html, body").animate({
				scrollTop: 0
			}, 1000);
			return false;
		});

		jQuery(window).on("scroll", function() {
			var scroll = jQuery(window).scrollTop();
			if (scroll > 900) {
				jQuery("button.scroltop").fadeIn(1000);
			} else {
				jQuery("button.scroltop").fadeOut(1000);
			}
		});
	}
	
// > input type file function by = custom.js ========================== //	 	 
	function input_type_file_form(){
		jQuery(document).on('change', '.btn-file :file', function() {
			var input = jQuery(this),
				numFiles = input.get(0).files ? input.get(0).files.length : 1,
				label = input.val().replace(/\\/g, 'https://thewebmax.org/').replace(/.*\//, '');
			input.trigger('fileselect', [numFiles, label]);
		});

		jQuery('.btn-file :file').on('fileselect', function(event, numFiles, label) {
			var input = jQuery(this).parents('.input-group').find(':text'),
				log = numFiles > 10 ? numFiles + ' files selected' : label;
			if (input.length) {
				input.val(log);
			} else {
				if (log) alert(log);
			}
		});	
	}

// > input Placeholder in IE9 function by = custom.js ======================== //	
	function placeholderSupport(){
	/* input placeholder for ie9 & ie8 & ie7 */
		jQuery.support.placeholder = ('placeholder' in document.createElement('input'));
		/* input placeholder for ie9 & ie8 & ie7 end*/
		/*fix for IE7 and IE8  */
		if (!jQuery.support.placeholder) {
			jQuery("[placeholder]").on('focus', function () {
				if (jQuery(this).val() === jQuery(this).attr("placeholder")) jQuery(this).val("");
			}).blur(function () {
				if (jQuery(this).val() === "") jQuery(this).val(jQuery(this).attr("placeholder"));
			}).blur();

			jQuery("[placeholder]").parents("form").on('submit', function () {
				jQuery(this).find('[placeholder]').each(function() {
					if (jQuery(this).val() === jQuery(this).attr("placeholder")) {
						 jQuery(this).val("");
					}
				});
			});
		}
		/*fix for IE7 and IE8 end */
	}	

	// > Nav submenu show hide on mobile by = custom.js
	function mobile_nav(){
		jQuery(".sub-menu").parent('li').addClass('has-child');
		jQuery("<div class='fa fa-angle-right submenu-toogle'></div>").insertAfter(".has-child > a");

		jQuery('.has-child a+.submenu-toogle').on('click',function(ev) {

			jQuery(this).parent().siblings(".has-child ").children(".sub-menu").slideUp(500, function(){
				jQuery(this).parent().removeClass('nav-active');
			});

			jQuery(this).next(jQuery('.sub-menu')).slideToggle(500, function(){
				jQuery(this).parent().toggleClass('nav-active');
			});

			ev.stopPropagation();
		});
	
	}
	 
	// Mobile side drawer function by = custom.js
	function mobile_side_drawer(){
		jQuery('#mobile-side-drawer').on('click', function () { 
			jQuery('.mobile-sider-drawer-menu').toggleClass('active');
		});
	}	
	
//  > Top Search bar Show Hide function by = custom.js =================== //	

	function site_search(){
		jQuery('a[href="#search"]').on('click', function(event) {                    
		jQuery('#search').addClass('open');
		jQuery('#search > form > input[type="search"]').focus();
	});
				
	jQuery('#search, #search button.close').on('click keyup', function(event) {
		if (event.target === this || event.target.className === 'close') {
			jQuery(this).removeClass('open');
		}
	});  
 	}	

//  Client logo Carousel function by = owl.carousel.js ========================== //
	function home_client_carousel(){
	jQuery('.home-client-carousel').owlCarousel({
		loop:true,
		nav:false,
		dots: true,				
		margin:5,
		autoplay:true,
		navText: ['<i class="fa fa-angle-left"></i>', '<i class="fa fa-angle-right"></i>'],
		responsive:{
			0:{
				items:2,
			},
			480:{
				items:3,
			},			
			767:{
				items:4,
			},
			1000:{
				items:4
			}
		}
	});
	}

	//  Client logo Carousel function by = owl.carousel.js ========================== //
	function home_client_carousel_2(){
		jQuery('.home-client-carousel2').owlCarousel({
			loop:true,
			nav:true,
			dots: false,				
			margin:30,
			autoplay:true,
			navText: ['<i class="fa fa-angle-left"></i>', '<i class="fa fa-angle-right"></i>'],
			responsive:{
				0:{
					items:2,
				},
				480:{
					items:3,
				},			
				767:{
					items:4,
				},
				1000:{
					items:6
				}
			}
		});
	}

	//  Client logo Carousel function by = owl.carousel.js ========================== //
	function home_client_carousel_3(){
		jQuery('.home-client-carousel3').owlCarousel({
			loop:true,
			nav:false,
			dots: false,				
			margin:30,
			autoplay:true,
			autoplayTimeout: 1500,
			navText: ['<i class="fa fa-angle-left"></i>', '<i class="fa fa-angle-right"></i>'],
			responsive:{
				0:{
					items:2,
				},
				480:{
					items:3,
				},			
				767:{
					items:4,
				},
				1000:{
					items:5
				}
			}
		});
	}

	//  Related jobs Carousel function by = owl.carousel.js ========================== //
	function twm_related_jobs_carousel(){
		jQuery('.twm-related-jobs-carousel').owlCarousel({
			loop:true,
			nav:false,
			dots: true,				
			margin:30,
			//autoplay:true,
			autoplayTimeout:3000,
			navText: ['<i class="fa fa-angle-left"></i>', '<i class="fa fa-angle-right"></i>'],
			responsive:{
				0:{
					items:1,
				},
				480:{
					items:1,
				},			
				767:{
					items:2,
				},
				1000:{
					items:3
				}
			}
		});
	}

	//  Client logo Carousel function by = owl.carousel.js ========================== //
	function home_client_carousel_4(){
		jQuery('.home-client-carousel4').owlCarousel({
			loop:true,
			nav:false,
			dots: false,				
			margin:0,
			autoplay:true,
			autoplayTimeout: 1500,
			navText: ['<i class="fa fa-angle-left"></i>', '<i class="fa fa-angle-right"></i>'],
			responsive:{
				0:{
					items:2,
				},
				480:{
					items:3,
				},			
				767:{
					items:4,
				},
				1000:{
					items:5
				}
			}
		});
	}

	//  Trusted logo Carousel function by = owl.carousel.js ========================== //
	function trusted_logo(){
		jQuery('.trusted-logo').owlCarousel({
			loop:true,
			nav:false,
			dots: false,				
			margin:5,
			autoplay:true,
			navText: ['<i class="fa fa-angle-left"></i>', '<i class="fa fa-angle-right"></i>'],
			responsive:{
				0:{
					items:1,
				},
				480:{
					items:2,
				},			
				767:{
					items:2,
				},
				991:{
					items:2
				}
			}
		});
	}

	//  Testimonial Carousel function by = owl.carousel.js ========================== //
	function twm_testimonial_1_carousel(){
		jQuery('.twm-testimonial-1-carousel').owlCarousel({
			loop:true,
			nav:true,
			dots: false,				
			margin:30,
			autoplay:true,
			navText: ['<i class="fa fa-angle-left"></i>', '<i class="fa fa-angle-right"></i>'],
			responsive:{
				0:{
					items:1,
				},
				480:{
					items:1,
				},			
				991:{
					items:2,
				}

			}
		});
	}
	
	//  Testimonial Carousel function by = owl.carousel.js ========================== //
	function twm_testimonial_2_carousel(){
		jQuery('.twm-testimonial-2-carousel').owlCarousel({
			loop:true,
			nav:true,
			dots: false,				
			margin:5,
			autoplay:true,
			navText: ['<i class="fa fa-angle-left"></i>', '<i class="fa fa-angle-right"></i>'],
			responsive:{
				0:{
					items:1,
				},
				480:{
					items:1,
				},			
				991:{
					items:2,
				},
				1199:{
					items:3,
				}

			}
		});
	}


	//  Latest Article Blogs Carousel function by = owl.carousel.js ========================== //
	function twm_la_home_blog(){
		jQuery('.twm-la-home-blog').owlCarousel({
			loop:true,
			nav:true,
			dots: false,				
			margin:30,
			autoplay:false,
			navText: ['<i class="fa fa-angle-left"></i>', '<i class="fa fa-angle-right"></i>'],
			responsive:{
				0:{
					items:1,
				},
				480:{
					items:1,
				},			
				991:{
					items:2,
				},
				1199:{
					items:3,
				}

			}
		});
	}

	//  Counter Section function by = counterup.min.js
	function counter_section(){
		jQuery('.counter').counterUp({
			delay: 10,
			time: 3000
		});	
	}	

		
	// sidebarCollapse function by = custom.js
	function msg_user_list_slide(){
		jQuery('.user-msg-list-btn-open, .user-msg-list-btn-close').on('click', function () { 
			jQuery('.wt-admin-dashboard-msg-2').toggleClass('active');
		});
	}		

	// sidebarCollapse function by = custom.js
	function sidebarCollapse(){
		jQuery('#sidebarCollapse').on('click', function () { 
			jQuery('#header-admin, #sidebar-admin-wraper, #content').toggleClass('active');
		});
	}

	// dashboard Notification function by = custom.js
	function dashboard_noti_dropdown(){
		jQuery('.dashboard-noti-dropdown').on('click', function () { 
			jQuery('.dashboard-noti-panel').toggleClass('active');
		});
	}	
	
	// dashboard Message function by = custom.js
	function dashboard_message_dropdown(){
		jQuery('.dashboard-message-dropdown').on('click', function () { 
			jQuery('.dashboard-message-panel').toggleClass('active');
		});
	}			

	// CustomScrollbar function by = jquery.scrollbar.js
	function scroll_bar_custome(){	
		jQuery('.scrollbar-macosx').scrollbar();
	}


	// Jobs Bookmark table function by = dataTables.bootstrap5.js
    function jobs_bookmark_table(){
        jQuery('#jobs_bookmark_table').DataTable(
            {     
                "aLengthMenu": [[3, 5, 10, -1], [3, 5, 10, "All"]],
                "iDisplayLength": 3
            } 
        );
    }
	
	// candidate_data_table function by = dataTables.bootstrap5.js
    function candidate_data_table(){
        jQuery('#candidate_data_table').DataTable(
            {     
                "aLengthMenu": [[5, 8, 10, -1], [5, 8, 10, "All"]],
                    "iDisplayLength": 5
                } 
            );

		function checkAll(bx) {
			var cbs = document.getElementsByTagName('input');
			for(var i=0; i < cbs.length; i++) {
				if(cbs[i].type == 'checkbox') {
				cbs[i].checked = bx.checked;
				}
			}
    	}
	}

	// datepicker function by = dbootstrap-datepicker.js
    function datepicker_function(){
		$('.datepicker').datepicker({
			format: 'dd/mm/yyyy'
		});
	}


	// profile-chart function by = chart.js
	function profile_chart(){
		if(jQuery('#profileViewChart').length){
			var profileViewChart = document.getElementById('profileViewChart').getContext('2d');
			var profileViewChart = new Chart(profileViewChart, {
				type: 'line',
				data: {
					labels: ['January', 'February', 'March', 'April', 'May', 'June'],
					datasets: [{
						label: 'Viewers',
						data: [200, 250, 350, 200, 250, 150],
						pointHoverBorderColor: '#1967d2',
						pointBorderWidth: 10,
						pointHoverBorderWidth: 3,
						pointHitRadius: 20,
						borderWidth: 3,
						borderColor: '#1967d2',
						pointBackgroundColor: 'rgba(255, 255, 255, 0)',
						pointHoverBackgroundColor: 'rgba(255, 255, 255, 1)',
						pointBorderColor: 'rgba(66, 133, 244, 0)',
						cubicInterpolationMode: 'monotone',
						fill: true,
						backgroundColor: 'rgba(212, 230, 255, 0.2)',
					}]
				},
			});
		}
	}


	// view map sidebar function by = custom.js
	function view_map_sidebar(){
		jQuery('.map-show-btn-open, .map-show-btn-close').on('click', function () { 
			jQuery('.half-map-section').toggleClass('active');
		});
	}
	//  Radius Range Slider function by = bootstrap-slider.min.js ========================== //
	function radius_range(){
		jQuery("#ex2").slider({});
	}

	//DropZone File Uploading Function Start=========================//
	function Dropzone_infut_file(){	
		if(jQuery('#demo-upload').length){
		var dropzone = new Dropzone('#demo-upload', {
		previewTemplate: document.querySelector('#preview-template').innerHTML,
		parallelUploads: 2,
		thumbnailHeight: 120,
		thumbnailWidth: 120,
		maxFilesize: 3,
		filesizeBase: 1000,
		thumbnail: function(file, dataUrl) {
			if (file.previewElement) {
			file.previewElement.classList.remove("dz-file-preview");
			var images = file.previewElement.querySelectorAll("[data-dz-thumbnail]");
			for (var i = 0; i < images.length; i++) {
				var thumbnailElement = images[i];
				thumbnailElement.alt = file.name;
				thumbnailElement.src = dataUrl;
			}
			setTimeout(function() { file.previewElement.classList.add("dz-image-preview"); }, 1);
			}
		}
	
		});
	
	
		// Now fake the file upload, since GitHub does not handle file uploads
		// and returns a 404
	
		var minSteps = 6,
			maxSteps = 60,
			timeBetweenSteps = 100,
			bytesPerStep = 100000;
	
		dropzone.uploadFiles = function(files) {
		var self = this;
	
		for (var i = 0; i < files.length; i++) {
	
			var file = files[i];
			totalSteps = Math.round(Math.min(maxSteps, Math.max(minSteps, file.size / bytesPerStep)));
	
			for (var step = 0; step < totalSteps; step++) {
			var duration = timeBetweenSteps * (step + 1);
			setTimeout(function(file, totalSteps, step) {
				return function() {
				file.upload = {
					progress: 100 * (step + 1) / totalSteps,
					total: file.size,
					bytesSent: (step + 1) * file.size / totalSteps
				};
	
				self.emit('uploadprogress', file, file.upload.progress, file.upload.bytesSent);
				if (file.upload.progress == 100) {
					file.status = Dropzone.SUCCESS;
					self.emit("success", file, 'success', null);
					self.emit("complete", file);
					self.processQueue();
					//document.getElementsByClassName("dz-success-mark").style.opacity = "1";
				}
				};
			}(file, totalSteps, step), duration);
			}
		}
		}
		}
	}
	//DropZone File Uploading Function End =========================//	


	//Maximum input box fields function Start by custom.js==============//

	var max_fields      = 100; //maximum input boxes allowed
	var wrapper   		= $(".input_fields_youtube"); //Fields wrapper
	var wrapper_2   		= $(".input_fields_vimeo"); //Fields wrapper
	var wrapper_3   		= $(".input_fields_custom"); //Fields wrapper
	var add_button_youtube      = $(".add_field_youtube"); //Add button ID
	var add_button_vimeo      = $(".add_field_vimeo"); //Add button ID
	var add_custom_field      = $(".add_field_custom"); //Add button ID
	
	var x = 1; //initlal text box count
	$(add_button_youtube).click(function(e){ //on add input button click
		e.preventDefault();
		if(x < max_fields){ //max input box allowed
			x++; //text box increment
			$(wrapper).append('<div class="ls-inputicon-box"><input class="form-control wt-form-control m-tb10" name="mytext[]" type="text" placeholder="https://www.youtube.com/"><i class="fs-input-icon fab fa-youtube"></i><a href="#" class="remove_field"><i class="fa fa-times"></i></a></div>'); //add input box
		}
	});
	
	var x = 1; //initlal text box count
	$(add_button_vimeo).click(function(e){ //on add input button click
		e.preventDefault();
		if(x < max_fields){ //max input box allowed
			x++; //text box increment
			$(wrapper_2).append('<div class="ls-inputicon-box"><input class="form-control m-tb10 wt-form-control" name="mytext[]" type="text" placeholder="https://vimeo.com/"><i class="fs-input-icon fab fa-vimeo-v"></i><a href="#" class="remove_field"><i class="fa fa-times"></i></a></div>'); //add input box
		}
	});	

	var x = 1; //initlal text box count
	$(add_custom_field).click(function(e){ //on add input button click
		e.preventDefault();
		if(x < max_fields){ //max input box allowed
			x++; //text box increment
			$(wrapper_3).append('<div class="ls-inputicon-box"><input class="form-control m-tb10 wt-form-control" name="mytext[]" type="text" placeholder="Selet the role that you work in"><i class="fs-input-icon fa fa-user"></i><a href="#" class="remove_field"><i class="fa fa-times"></i></a></div>'); //add input box
		}
	});	
	
	$(wrapper).on("click",".remove_field", function(e){ //user click on remove text
		e.preventDefault(); $(this).parent('div').remove(); x--;
	})
	$(wrapper_2).on("click",".remove_field", function(e){ //user click on remove text
		e.preventDefault(); $(this).parent('div').remove(); x--;
	})	
	$(wrapper_3).on("click",".remove_field", function(e){ //user click on remove text
		e.preventDefault(); $(this).parent('div').remove(); x--;
	})	
	
//Maximum input box fields function End by custom.js==============//

// > Tooltip function by = isotope.pkgd.min.js ========================= //
	var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
	var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
	return new bootstrap.Tooltip(tooltipTriggerEl)
})
/*--------------------------------------------------------------------------------------------
	Window on load ALL FUNCTION START
---------------------------------------------------------------------------------------------*/
	// > masonry function function by = isotope.pkgd.min.js ========================= //	

	function masonryBox() {
		if ( jQuery().isotope ) {      
			var $container = jQuery('.masonry-wrap');
				$container.isotope({
					itemSelector: '.masonry-item',
					transitionDuration: '1s',
					originLeft: true,
					stamp: '.stamp',
				});

			$container.imagesLoaded().progress( function() {
				$container.isotope('layout');
			});

			jQuery('.masonry-filter li').on('click',function() {                           
				var selector = jQuery(this).find("a").attr('data-filter');
				jQuery('.masonry-filter li').removeClass('active');
				jQuery(this).addClass('active');
				$container.isotope({ filter: selector });
				return false;
			});
		};
	}
	

// > page loader function by = custom.js ========================= //		
	function page_loader() {
		$('.loading-area').fadeOut(1000);
	}

/*--------------------------------------------------------------------------------------------
    Window on scroll ALL FUNCTION START
---------------------------------------------------------------------------------------------*/

    function color_fill_header() {
        var scroll = $(window).scrollTop();
        if(scroll >= 100) {
            $(".is-fixed").addClass("color-fill");
        } else {
            $(".is-fixed").removeClass("color-fill");
        }
    }
	

/*--------------------------------------------------------------------------------------------
	document.ready ALL FUNCTION START
---------------------------------------------------------------------------------------------*/
	jQuery(document).ready(function() {
		//  selectpicker function by = bootstrap-select.min.js ========================== //
	    select_picker_select(),
		//  Home 1 Banner Carousel function by = owl.carousel.js ========================== //
	    twm_h1_bnr_carousal(),
		//  Job Categories Carousel function by = owl.carousel.js ========================== //
	    job_categories_carousel(),
		// > Top Search bar Show Hide function by = custom.js  		
		site_search(),	
		// > Video responsive function by = custom.js 
		video_responsive(),
		 // > LIGHTBOX Gallery Popup function	by = lc_lightbox.lite.js =========================== //      
		lightbox_popup(),
		// > magnificPopup for video function	by = magnific-popup.js
		magnific_video(),
		// > Vertically center Bootstrap modal popup function by = custom.js
		popup_vertical_center();
		// > Main menu sticky on top  when scroll down function by = custom.js		
		sticky_header(),
	    // > Sidebar sticky  when scroll down function by = theia-sticky-sidebar.js ========== //		
		sticky_sidebar(),
		// > page scroll top on button click function by = custom.js	
		scroll_top(),
		// > input type file function by = custom.js	 	
		input_type_file_form(),
		// > input Placeholder in IE9 function by = custom.js		
		placeholderSupport(),
		// > Nav submenu on off function by = custome.js ===================//
		mobile_nav(),
		// Mobile side drawer function by = custom.js
		mobile_side_drawer(),
		//  Client logo Carousel function by = owl.carousel.js ========================== //
		home_client_carousel(),
		//  Client logo Carousel function by = owl.carousel.js ========================== //
	    home_client_carousel_2(),
		//  Client logo Carousel function by = owl.carousel.js ========================== //
	    home_client_carousel_3(),
		//  Related jobs Carousel function by = owl.carousel.js ========================== //
	    twm_related_jobs_carousel(),
		//  Client logo Carousel function by = owl.carousel.js ========================== //
	    home_client_carousel_4(),
		//  Trusted logo Carousel function by = owl.carousel.js ========================== //
		trusted_logo(),
		//  Testimonial Carousel function by = owl.carousel.js ========================== //
	    twm_testimonial_1_carousel(),
		//  Testimonial Carousel function by = owl.carousel.js ========================== //
	    twm_testimonial_2_carousel(),
		//  Latest Article Blogs Carousel function by = owl.carousel.js ========================== //
		twm_la_home_blog(),
		//  Counter Section function by = counterup.min.js ========================== //
		counter_section(),
		//massage user list show hide function by = custom.js	 ========================== //
		msg_user_list_slide(),
		// sidebarCollapse function by = custom.js
		sidebarCollapse(),
		// dashboard Notification function by = custom.js
	    dashboard_noti_dropdown(),	
		// dashboard Message function by = custom.js
		dashboard_message_dropdown(),
		// CustomScrollbar function by = jquery.scrollbar.js	
		scroll_bar_custome(),
		// Jobs Bookmark table function by = dataTables.bootstrap5.js
		jobs_bookmark_table(),
		// candidate_data_table function by = dataTables.bootstrap5.js
		candidate_data_table(),
		// datepicker function by = dbootstrap-datepicker.js
		datepicker_function(),
		// profile-chart function by = chart.js
		profile_chart(),
		// view map sidebar function by = custom.js
	    view_map_sidebar(),
		//  Radius Range Slider function by = bootstrap-slider.min.js ========================== //
	     radius_range(),
		//DropZone File Uploading Function Start=========================//
	    Dropzone_infut_file();
			
	}); 	

/*--------------------------------------------------------------------------------------------
	Window Load START
---------------------------------------------------------------------------------------------*/
jQuery(window).on('load', function () {
	// > masonry function function by = isotope.pkgd.min.js		
	masonryBox(),
	// > page loader function by = custom.js		
	page_loader();
});

 /*===========================
	Window Scroll ALL FUNCTION START
===========================*/

jQuery(window).on('scroll', function () {
// > Window on scroll header color fill 
	color_fill_header();
});
	

/*===========================
	Document on  Submit FUNCTION START
===========================*/

	// > Contact form function by = custom.js	
	jQuery(document).on('submit', 'form.cons-contact-form', function(e){
		e.preventDefault();
		var form = jQuery(this);
		/* sending message */
		jQuery.ajax({
			url: 'https://thewebmax.com/jobzilla/form-handler2.php',
			
			data: form.serialize() + "&action=contactform",
			type: 'POST',
			dataType: 'JSON',
			beforeSend: function() {
				jQuery('.loading-area').show();
			},

			success:function(data){
				jQuery('.loading-area').hide();
				if(data['success']){
				jQuery("<div class='alert alert-success'>"+data['message']+"</div>").insertBefore('form.cons-contact-form');
				}else{
				jQuery("<div class='alert alert-danger'>"+data['message']+"</div>").insertBefore('form.cons-contact-form');	
				}
			}
		});
		jQuery('.cons-contact-form').trigger("reset");
		return false;
	});

/*===========================
	Document on  Submit FUNCTION END
===========================*/	


	/*upload profile pic function*/

    const fileUploader = document.getElementById('file-uploader');
    const reader = new FileReader();
    const imageGrid = document.getElementById('upload-image-grid');
	if(fileUploader){
		fileUploader.addEventListener('change', (event) => {
			const files = event.target.files;
			const file = files[0];
			
			const img = document.createElement('img');
			imageGrid.appendChild(img);
			img.src = URL.createObjectURL(file);
			img.alt = file.name;
		});
		
	}

	
})(window.jQuery);