jQuery(document).ready(function($) {
    "use strict";

    // menu
    $(".level1_h1 .level11 a").on("click", function() {
        $(this).parent().parent().find("level11").removeClass("active").addClass("active");

    });
    $(".level1_h1 .level11 a").on("hover", function() {
        $(this).parent().parent().find("level11").addClass("active");

    });

    $("#open-filters").on("click", function() {
        $(this).toggleClass("hamburger-icon");
    })
    // home2
    var fixSpaceTabSlick = function(display) {
        var tabList = $('.js-tab-product');
        $.each(tabList, function() {
            var check = $(this).attr('id');
            if (check == display) {
                $(this).show();
                $(this).slick('setPosition');
            } else {
                $(this).hide();
            }
        });
    }
    // End/menu

    // categories

    $('a[data-toggle="tab"]').on('show.bs.tab', function(e) {
        fixSpaceTabSlick($(this).attr('aria-controls'));
    });

    $('.js-tab-product').slick({
        infinite: true,
        slidesToShow: 5,
        arrows: true,
        slidesToScroll: 1,
        dots: false,
        responsive: [{
                breakpoint: 991,
                settings: {
                    slidesToShow: 3,

                }
            },
            {
                breakpoint: 769,
                settings: {
                    slidesToShow: 2,

                }
            },
            {
                breakpoint: 450,
                settings: {
                    slidesToShow: 1,

                }
            },

        ]
    });

    fixSpaceTabSlick($('.product-tab-slide .nav-tabs li[class*="active"] > a').attr('aria-controls'));
    $('.js-categories-prd-dtails1').slick({
        infinite: true,
        slidesToShow: 4,
        arrows: true,
        slidesToScroll: 1,
        dots: false,
        responsive: [{
                breakpoint: 991,
                settings: {
                    slidesToShow: 3,

                }
            },
            {
                breakpoint: 769,
                settings: {
                    slidesToShow: 2,

                }
            },
            {
                breakpoint: 450,
                settings: {
                    slidesToShow: 1,

                }
            },

        ]
    });

    // end/categories

    // product
    var $productSlick = $('.js-mobi-product');
    var detectViewPort = function() {
        var viewPortWidth = $(window).width();
        if (viewPortWidth < 769) {
            if (!$productSlick.hasClass('slick-initialized')) {
                $('.js-mobi-product').slick({
                    slidesToShow: 2,
                    slidesToScroll: 1,
                    dots: false,
                    arrows: true,
                    responsive: [{
                        breakpoint: 480,
                        settings: {
                            slidesToShow: 1,
                        }
                    }]
                });
            }
        } else {
            if ($productSlick.hasClass('slick-initialized')) {
                $('.js-mobi-product').slick('destroy');
            }
        }
    };

    detectViewPort();
    $(window).resize(function() {
        detectViewPort();
    });

    setTimeout(function() {
        $('body').addClass('loaded');
    }, 2000);
    // end/product
    // search
    $(".close-search-form").on("click", function() {
        $('.menubar-search-form').removeClass('js-open-search');
    });
    // end/search

    // user
    $(".click-hover-user").on("click", function() {
        $(".submenu_user").css("opacity", "1");
        $(".submenu_user").css("visibilyti", "inherit");
    });
    // end / user


    $(".dropdown").on("hover", function() {
            $('.dropdown-menu', this).stop(true, true).slideDown("fast");
            $(this).toggleClass('open');
        },
        function() {
            $('.dropdown-menu', this).stop(true, true).slideUp("fast");
            $(this).toggleClass('open');
        }
    );

    $('select.selectpicker').selectpicker({
        caretIcon: 'glyphicon glyphicon-menu-down',
    });



    // slide price
    if ($("#price").length) {
        var slider = new Slider('#price', {});
    }
    $(".noo-menu").on("click", function() {
        var slide = $(this).find('.sub-menu').slideToggle(600);
    })


    // slick


    $('.js-team').slick({
        infinite: true,
        slidesToShow: 5,
        arrows: true,
        slidesToScroll: 1,
        dots: false,
        responsive: [{
                breakpoint: 991,
                settings: {
                    slidesToShow: 4,
                    dots: true,
                    arrows: false,
                }
            },
            {
                breakpoint: 769,
                settings: {
                    slidesToShow: 2,
                    dots: true,
                    arrows: false,
                }
            },
            {
                breakpoint: 450,
                settings: {
                    slidesToShow: 1,
                    dots: true,
                    arrows: false,

                }
            },

        ]
    });
    $('.slider-for-dt2').slick({

        slidesToShow: 1,
        slidesToScroll: 1,
        arrows: false,
        dots: false,
        fade: true,
        infinite: false,
        asNavFor: '.slider-nav-dt2',
        responsive: [{
            breakpoint: 991,
            settings: {
                dots: true
            }
        }]
    });

    $('.slider-nav-dt2').slick({
        slidesToShow: 2,
        slidesToScroll: 1,
        asNavFor: '.slider-for-dt2',
        arrows: true,
        dots: false,
        infinite: false,
        vertical: true,
        verticalSwiping: true,
        focusOnSelect: true,
        responsive: [{
                breakpoint: 991,
                settings: {
                    slidesToShow: 2,
                    vertical: false,
                    verticalSwiping: false,
                    focusOnSelect: false,
                }
            },

        ]
    });
    $('.js-slideshow').slick({
        infinite: true,
        slidesToShow: 1,
        arrows: true,
        slidesToScroll: 1,
        dots: false

    });
    $('.home-2').slick({
        infinite: true,
        slidesToShow: 5,
        arrows: true,
        slidesToScroll: 1,
        dots: false,
        responsive: [{
                breakpoint: 991,
                settings: {
                    slidesToShow: 3,

                }
            },
            {
                breakpoint: 769,
                settings: {
                    slidesToShow: 2,

                }
            },
            {
                breakpoint: 450,
                settings: {
                    slidesToShow: 1,

                }
            },

        ]
    });
    $('.js-slide-brand').slick({
        infinite: true,
        slidesToShow: 6,
        arrows: false,
        slidesToScroll: 1,
        dots: false,
        responsive: [{
                breakpoint: 991,
                settings: {
                    slidesToShow: 4,

                }
            },
            {
                breakpoint: 769,
                settings: {
                    slidesToShow: 3,

                }
            },
            {
                breakpoint: 450,
                settings: {
                    slidesToShow: 2,

                }
            },

        ]
    });
    $('.slider-for').slick({
        slidesToShow: 1,
        slidesToScroll: 1,
        arrows: false,
        fade: true,
        asNavFor: '.slider-nav'
    });
    $('.slider-nav').slick({
        slidesToShow: 4,
        slidesToScroll: 1,
        asNavFor: '.slider-for',
        arrows: true,
        leftMode: true,
        focusOnSelect: true,
        responsive: [{
            breakpoint: 480,
            settings: {
                slidesToShow: 2,
            }
        }]
    });
    // End/slick
    // number
    var quantitiy = 0;

    $('.js-minus').on("click", function(e) {
        e.preventDefault();
        var quantity = parseInt($('.js-number').val(), 10);
        $('.js-number').val(quantity + 1);
    });

    $('.js-plus').on("click", function(e) {
        e.preventDefault();
        var quantity = parseInt($('.js-number').val(), 10);
        if (quantity > 0) {
            $('.js-number').val(quantity - 1);
        }
    });
    // end/number

    // ordering
    $(".ordering .list").on("click", function() {
        $(this).toggleClass("active");
        $(".item").addClass("list-item");
        $(".ordering .col").removeClass("active");
        $(".col-remove").removeClass("col-md-4");
        $(".col-remove").removeClass("col-md-3");
        $(".act-img").toggleClass("act-img-click");
        $(".img-ic").toggleClass("img-ic-click");

    });
    $(".ordering .col").on("click", function() {
        $(this).toggleClass("active");
        $(".item").removeClass("list-item");
        $(this).removeClass("active");
        $(".act-img").toggleClass("act-img-click");
        $(".img-ic").toggleClass("img-ic-click");

        // end/ordering
    });
    /*MAP*/
    function init() {
        var mapOptions = {
            zoom: 14,
            center: new google.maps.LatLng(40.6933804, -74.0196236),
            styles: [{
                "featureType": "administrative.province",
                "elementType": "all",
                "stylers": [{
                    "visibility": "off"
                }]
            }, {
                "featureType": "landscape",
                "elementType": "all",
                "stylers": [{
                    "saturation": -100
                }, {
                    "lightness": 65
                }, {
                    "visibility": "on"
                }]
            }, {
                "featureType": "poi",
                "elementType": "all",
                "stylers": [{
                    "saturation": -100
                }, {
                    "lightness": 51
                }, {
                    "visibility": "simplified"
                }]
            }, {
                "featureType": "road.highway",
                "elementType": "all",
                "stylers": [{
                    "saturation": -100
                }, {
                    "visibility": "simplified"
                }]
            }, {
                "featureType": "road.arterial",
                "elementType": "all",
                "stylers": [{
                    "saturation": -100
                }, {
                    "lightness": 30
                }, {
                    "visibility": "on"
                }]
            }, {
                "featureType": "road.local",
                "elementType": "all",
                "stylers": [{
                    "saturation": -100
                }, {
                    "lightness": 40
                }, {
                    "visibility": "on"
                }]
            }, {
                "featureType": "transit",
                "elementType": "all",
                "stylers": [{
                    "saturation": -100
                }, {
                    "visibility": "simplified"
                }]
            }, {
                "featureType": "transit",
                "elementType": "geometry.fill",
                "stylers": [{
                    "visibility": "on"
                }]
            }, {
                "featureType": "water",
                "elementType": "geometry",
                "stylers": [{
                    "hue": "#ffff00"
                }, {
                    "lightness": -25
                }, {
                    "saturation": -97
                }]
            }, {
                "featureType": "water",
                "elementType": "labels",
                "stylers": [{
                    "visibility": "on"
                }, {
                    "lightness": -25
                }, {
                    "saturation": -100
                }]
            }]
        };
        var mapElement = document.getElementById('map');
        var map = new google.maps.Map(mapElement, mapOptions);
        var marker = new google.maps.Marker({
            position: new google.maps.LatLng(40.6933804, -74.0196236),
            map: map,
            title: 'Snazzy!'
        });
    }
    if ($('#map').length > 0) {
        google.maps.event.addDomListener(window, 'load', init);

    }
    /*END/MAP*/


    // Slider
    $(function() {
        initSlide();
        $('.slider__show').on('beforeChange', function(event, slick, currentSlide, nextSlide) {
            initInfo();
        });
    });

    function initSlide() {
        $('.slideshow-item').slick({
            slidesToShow: 1,
            autoplay: true,
            autoplaySpeed: 1000,
            arrows: false
        });


        $('.slider__show').slick({
            centerMode: true,
            slidesToShow: 3,
            centerPadding: '0px',
            autoplaySpeed: 1000,
            arrows: false,
            responsive: [{
                    breakpoint: 769,
                    settings: {
                        slidesToShow: 3,
                    }
                },
                {
                    breakpoint: 569,
                    settings: {
                        slidesToShow: 1,
                        dots: true,
                    }

                },
                {
                    breakpoint: 321,
                    settings: {
                        slidesToShow: 1,
                        dots: true,
                    }
                },
            ]
        });

        initInfo();

    }


    function initInfo() {
        var itemCurr = $('.slider__show .slick-current');
        $('.slider__meta > .name').html(itemCurr.data('name'));
        $('.slider__meta > .position').html(itemCurr.data('position'));
        $('.slider__meta > .desc').html(itemCurr.data('desc'));
    }
    // End/Slider


    // ENGO_CountDown
    $.fn.ENGO_CountDown = function(options) {
        return this.each(function() {
            new $.ENGO_CountDown(this, options);
        });
    }
    $.ENGO_CountDown = function(obj, options) {
        var ddiff, gsecs;
        this.options = $.extend({
            autoStart: true,
            LeadingZero: true,
            DisplayFormat: "<div><span>%%D%% :</span> Days</div><div><span>%%H%% :</span> Hours</div><div><span>%%M%% :</span> Mins</div><div><span>%%S%% :</span> Secs</div>",
            FinishMessage: "Expired",
            CountActive: true,
            TargetDate: null
        }, options || {});
        if (this.options.TargetDate == null || this.options.TargetDate == '') {
            return;
        }
        this.timer = null;
        this.element = obj;
        this.CountStepper = -1;
        this.CountStepper = Math.ceil(this.CountStepper);
        this.SetTimeOutPeriod = (Math.abs(this.CountStepper) - 1) * 1000 + 990;
        var dthen = new Date(this.options.TargetDate);
        var dnow = new Date();
        if (this.CountStepper > 0) {
            ddiff = new Date(dnow - dthen);
        } else {
            ddiff = new Date(dthen - dnow);
        }
        gsecs = Math.floor(ddiff.valueOf() / 1000);
        this.CountBack(gsecs, this);
    };
    $.ENGO_CountDown.fn = $.ENGO_CountDown.prototype;
    $.ENGO_CountDown.fn.extend = $.ENGO_CountDown.extend = $.extend;
    $.ENGO_CountDown.fn.extend({
        calculateDate: function(secs, num1, num2) {
            var s = ((Math.floor(secs / num1)) % num2).toString();
            if (this.options.LeadingZero && s.length < 2) {
                s = "0" + s;
            }
            return "<b>" + s + "</b>";
        },
        CountBack: function(secs, self) {
            var DisplayStr;
            if (secs < 0) {
                self.element.innerHTML = '<div class="labelexpired"> ' + self.options.FinishMessage + "</div>";
                return;
            }
            clearInterval(self.timer);
            DisplayStr = self.options.DisplayFormat.replace(/%%D%%/g, self.calculateDate(secs, 86400, 100000));
            DisplayStr = DisplayStr.replace(/%%H%%/g, self.calculateDate(secs, 3600, 24));
            DisplayStr = DisplayStr.replace(/%%M%%/g, self.calculateDate(secs, 60, 60));
            DisplayStr = DisplayStr.replace(/%%S%%/g, self.calculateDate(secs, 1, 60));
            self.element.innerHTML = DisplayStr;
            if (self.options.CountActive) {
                self.timer = null;
                self.timer = setTimeout(function() {
                    self.CountBack((secs + self.CountStepper), self);
                }, (self.SetTimeOutPeriod));
            }
        }

    });

    function init_countdown() {
        /** Countdown **/
        $('[data-countdown="countdown"]').each(function(index, el) {
            var $this = $(this);
            var $date = $this.data('date').split("-");
            $this.ENGO_CountDown({
                TargetDate: $date[0] + "/" + $date[1] + "/" + $date[2] + " " + $date[3] + ":" + $date[4] + ":" + $date[5],
                DisplayFormat: "<li><p>%%D%% <span>:</span> </p><span>days</span></li><li><p>%%H%% <span>:</span></p><span>hrs</span></li><li><p>%%M%% <span>:</span> </p><span>mins</span></li><li><p>%%S%% </p><span>secs</span></li>",
                FinishMessage: "Expired"
            });
        });

    }

    function init_countdown_prd() {
        $('[data-countdown="countdown_prd"]').each(function(index, el) {
            var $this = $(this);
            var $date = $this.data('date').split("-");
            $this.ENGO_CountDown({
                TargetDate: $date[0] + "/" + $date[1] + "/" + $date[2] + " " + $date[3] + ":" + $date[4] + ":" + $date[5],
                DisplayFormat: "<li><p>%%D%% <span>:</span> </p></li><li><p>%%H%% <span>:</span></p></li><li><p>%%M%% <span>:</span> </p</li><li><p>%%S%% </p></li>",
                FinishMessage: "Expired"
            });
        });

    }
    init_countdown_prd();
    init_countdown();
    // End/ENGO_CountDown



    // toggleClass
    $('#open-filters').on("click", function() {
        $('.left-slidebar').toggleClass('open-fil');

    });
    $('.js-click-config').on("click", function() {
        $('.sidenav').toggleClass('mySidenav');

    })
    $(".btn-navbar").on("click", function() {
        $(".off-canvas-nav").toggleClass('open-canvas-nav');
    })
    $('.js-click-cart').on("click", function() {
        $('.overlay').toggleClass('myNav');

    })
    // end/toggleClass
    // search
    $('.js-click-search-mobi').on("click", function() {
        $('.menubar-search-form').toggleClass('js-open-search');

    });
    // submenu_user
    $('.js-click-user').on("click", function() {
        $('.submenu_user').toggleClass('js-open-user');

    });
    // myNav

    // removeClass
    $('.closebtn').on("click", function() {
        $('.overlay').removeClass('myNav');
    })


    $('.close').on("click", function() {
        $('.sidenav').removeClass('mySidenav');

    })

    $(".remove-menumobile").on("click", function() {
        $(".off-canvas-nav").removeClass('open-canvas-nav');
    })
    // end/removeClass


});