<!DOCTYPE html>
<html>
	<head>

		<!-- Basic -->
		<meta charset="utf-8">
		<meta http-equiv="X-UA-Compatible" content="IE=edge">	

		<title>LaTeXer</title>	

		<meta name="keywords" content="LaTeX" />
		<meta name="description" content="LaTeXer - Turn your handwritten equations into LaTeX with ease!">
		<meta name="author" content="Radi">

		<!-- Favicon -->
		<link rel="shortcut icon" href="img/favicon.ico" type="image/x-icon" />
		<link rel="apple-touch-icon" href="img/apple-touch-icon.png">

		<!-- Mobile Metas -->
		<meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0">

		<!-- Web Fonts  -->
		<link href="https://fonts.googleapis.com/css?family=Poppins:300,400,500,600,700" rel="stylesheet" type="text/css">

		<!-- Vendor CSS -->
		<link rel="stylesheet" href="<?php echo base_url('public/'); ?>vendor/bootstrap/css/bootstrap.min.css">
		<link rel="stylesheet" href="<?php echo base_url('public/'); ?>vendor/font-awesome/css/font-awesome.min.css">
		<link rel="stylesheet" href="<?php echo base_url('public/'); ?>vendor/animate/animate.min.css">
		<link rel="stylesheet" href="<?php echo base_url('public/'); ?>vendor/simple-line-icons/css/simple-line-icons.min.css">
		<link rel="stylesheet" href="<?php echo base_url('public/'); ?>vendor/owl.carousel/assets/owl.carousel.min.css">
		<link rel="stylesheet" href="<?php echo base_url('public/'); ?>vendor/owl.carousel/assets/owl.theme.default.min.css">
		<link rel="stylesheet" href="<?php echo base_url('public/'); ?>vendor/magnific-popup/magnific-popup.min.css">

		<!-- Theme CSS -->
		<link rel="stylesheet" href="<?php echo base_url('public/'); ?>css/theme.css">
		<link rel="stylesheet" href="<?php echo base_url('public/'); ?>css/theme-elements.css">
		<link rel="stylesheet" href="<?php echo base_url('public/'); ?>css/theme-blog.css">
		<link rel="stylesheet" href="<?php echo base_url('public/'); ?>css/theme-shop.css">

		<!-- Current Page CSS -->
		<link rel="stylesheet" href="<?php echo base_url('public/'); ?>vendor/rs-plugin/css/settings.css">
		<link rel="stylesheet" href="<?php echo base_url('public/'); ?>vendor/rs-plugin/css/layers.css">
		<link rel="stylesheet" href="<?php echo base_url('public/'); ?>vendor/rs-plugin/css/navigation.css">
		
		<!-- Demo CSS -->
		<link rel="stylesheet" href="<?php echo base_url('public/'); ?>css/demos/demo-app-landing.css">

		<!-- Skin CSS -->
		<link rel="stylesheet" href="<?php echo base_url('public/'); ?>css/skins/skin-app-landing.css"> 

		<!-- Theme Custom CSS -->
		<link rel="stylesheet" href="<?php echo base_url('public/'); ?>css/custom.css">

		<!-- Head Libs -->
		<script src="<?php echo base_url('public/'); ?>vendor/modernizr/modernizr.min.js"></script>

	</head>
	<body>
		<body data-spy="scroll" data-target=".header-nav-main nav" data-offset="65">
		
			<div role="main" class="main">

				<section id="overview" class="section custom-background-color-1 m-0">
					<div class="container">
						<div class="row">
							<div class="">
								<div class="custom-top-title-box">
									<!-- <span class="text-color-light font-weight-semibold">CHECK OUT THE ONLY</span> -->
									<h1 class="text-color-light">LaTeXer</h1>
									<span class="text-color-light font-weight-semibold mb-5">Turn your handwritten equations into <i style="font-size: 120%;"> LaTeX </i> with ease!</span>
									
								</div>
							</div>
						</div>
						<?php if(!empty($errors)){ ?>
							<div class="row">
								<div class="mx-auto">
									<center>
										<?php foreach ($errors as $error) { ?>
											<?php echo "<h3 class='text-color-light font-weight-semibold mb-5'>" . $error . "</h3>"; ?>
										<?php } ?>
									</center>
								</div>
							</div>
						<?php } ?>
						<?php if(!empty($svg)){ ?>
							<div class="row">
								<div class="col-md-4">
									<h4 class="text-color-light text-right">Equation:</h4>
								</div>
								<div class="col-md-8">
									<div class="custom-btn-style-2 text-color-light text-center" readonly disabled style="border-radius:10px; margin-bottom: 5%; width: 100%;">
										<?php echo $svg; ?>
									</div>
								</div>
							</div>
						<?php } ?>
						<?php if(!empty($latex)){ ?>
							<div class="row">
								<div class="col-md-4">
									<h4 class="text-color-light text-right">LaTeX:</h4>
								</div>
								<div class="col-md-8">
									<div class="custom-btn-style-2 text-color-light text-center" readonly disabled style="border-radius:10px; margin-bottom: 5%; width: 100%;">
										<?php echo $latex; ?>
									</div>
								</div>
							</div>
						<?php } ?>
						<div class="row">
							<div class="mx-auto">
								<center>
									<form class="md-form" method="post" enctype="multipart/form-data">
									  <div class="file-field">
									      <input type="file" id="image" name="image" class="btn btn-primary custom-btn-style-1 _borders text-color-light ml-2 mb-2" required>
									  </div>
									  <div id="image_preview">
									  	
									  </div>
									  <div class="file-field">
									      <input class="btn btn-primary custom-btn-style-1 _borders text-color-light ml-2 mb-2" type="submit" value="Get Latex Format">
									  </div>
									</form>
								</center>
							</div>
						</div>
					</div>
				</section>

				

			<footer id="footer" class="background-color-light">
				
				<div class="footer-copyright background-color-light">
					<div class="container">
						<div class="row">
							<div class="col-lg-6 text-center text-md-left">
								<span class="copyright-text">
									© Copyright 2019. All Rights Reserved.
								</span>
							</div>
							<div class="col-lg-6 text-center text-md-right">
								<span class="copyright-text">
									ASU CVC'19 - Majestics
								</span>
							</div>
						</div>
					</div>
				</div>
			</footer>
		</div>

		<!-- Vendor -->
		<script src="<?php echo base_url('public/'); ?>vendor/jquery/jquery.min.js"></script>
		<script src="<?php echo base_url('public/'); ?>vendor/jquery.appear/jquery.appear.min.js"></script>
		<script src="<?php echo base_url('public/'); ?>vendor/jquery.easing/jquery.easing.min.js"></script>
		<script src="<?php echo base_url('public/'); ?>vendor/jquery-cookie/jquery-cookie.min.js"></script>
		<script src="<?php echo base_url('public/'); ?>vendor/popper/umd/popper.min.js"></script>
		<script src="<?php echo base_url('public/'); ?>vendor/bootstrap/js/bootstrap.min.js"></script>
		<script src="<?php echo base_url('public/'); ?>vendor/common/common.min.js"></script>
		<script src="<?php echo base_url('public/'); ?>vendor/jquery.validation/jquery.validation.min.js"></script>
		<script src="<?php echo base_url('public/'); ?>vendor/jquery.easy-pie-chart/jquery.easy-pie-chart.min.js"></script>
		<script src="<?php echo base_url('public/'); ?>vendor/jquery.gmap/jquery.gmap.min.js"></script>
		<script src="<?php echo base_url('public/'); ?>vendor/jquery.lazyload/jquery.lazyload.min.js"></script>
		<script src="<?php echo base_url('public/'); ?>vendor/isotope/jquery.isotope.min.js"></script>
		<script src="<?php echo base_url('public/'); ?>vendor/owl.carousel/owl.carousel.min.js"></script>
		<script src="<?php echo base_url('public/'); ?>vendor/magnific-popup/jquery.magnific-popup.min.js"></script>
		<script src="<?php echo base_url('public/'); ?>vendor/vide/vide.min.js"></script>
		
		<!-- Theme Base, Components and Settings -->
		<script src="js/theme.js"></script>
		
		<!-- Current Page Vendor and Views -->
		<script src="<?php echo base_url('public/'); ?>vendor/rs-plugin/js/jquery.themepunch.tools.min.js"></script>
		<script src="<?php echo base_url('public/'); ?>vendor/rs-plugin/js/jquery.themepunch.revolution.min.js"></script>

		<!-- Current Page Vendor and Views -->
		<script src="<?php echo base_url('public/'); ?>js/views/view.contact.js"></script>

		<!-- Demo -->
		<script src="<?php echo base_url('public/'); ?>js/demos/demo-app-landing.js"></script>
		
		<!-- Theme Custom -->
		<script src="<?php echo base_url('public/'); ?>js/custom.js"></script>
		
		<!-- Theme Initialization Files -->
		<script src="<?php echo base_url('public/'); ?>js/theme.init.js"></script>

		<script>
			$(document).ready(function() 
			{ 
				$('#image').change(function(){
					 var total_file=document.getElementById("image").files.length;
					 for(var i=0;i<total_file;i++)
					 {
						  $('#image_preview').html("<img style='height: 200px; width: auto; margin:5%;' id='"+ i +"' src='"+URL.createObjectURL(event.target.files[i])+"'>");
					 }
				});
			});
			</script>
	</body>
</html>