$(function(){
	if ($('.visual .images').size()>0) {
		$('.product-block .visual .images .switchers li a').click(function(){
			$('.product-block .visual .images .frame>img').attr('src',$(this).attr('href'));
			$('.product-block .visual .images .frame .title span').text($('img',this).attr('alt'));
			return false;
		});
	}
	if ($('.slider').size()>0) {
		$('.slider').fadeGalleryNews();
	}
	BtnHolder= $(".house-list li .btn-holder");
	changeClass();
	changeBtnWidth();
	$(window).resize(function(){
		changeClass();
		changeBtnWidth();
	});
	$('form .title .more').click(function(){
		if ($(this).is('.active')) {
			$(this).removeClass('active').parent().nextAll().not(".btn-holder").hide();
		} else {
			$(this).addClass('active').parent().nextAll().not(".btn-holder").show();;
		}
		return false;
	});
	$('.slider .frame ul li .info .title').textShadow();
});
var BtnHolder = []; 
function changeBtnWidth() {
	$('a',BtnHolder).css('width', "auto");
	var btnsWidth  = 0;
	BtnHolder.each(function(){
		btnsWidth =0;
		$('a',this).each(function(){
			btnsWidth += $(this).outerWidth(true);
		});
		var addWidth = Math.floor((BtnHolder.width()-btnsWidth)/2 - 1);
		$('a',this).each(function(){
			$(this).css("width","+="+addWidth);
		});
	});
}
function changeClass() {
	var w = $(window).width();
	if (w<1576){
		if (w<1177){
			if (w<745) {
				$('body').removeClass("width1200 width768").addClass('width640');
			} else {
				$('body').removeClass("width640 width1200").addClass('width768');
			}
		} else {
			$('body').removeClass("width640 width768").addClass('width1200');
		}
	} else {
		$('body').removeClass("width640 width768 width1200");
	}
}
jQuery.fn.fadeGalleryNews = function(_options){
	var _options = jQuery.extend({
		slideElements:'.frame li',
		pagerLinks:'.switchers li',
		btnNext:'a.next',
		btnPrev:'a.prev',
		btnPlayPause:'a.play-pause',
		pausedClass:'paused',
		playClass:'playing',
		activeClass:'active',
		pauseOnHover:true,
		autoRotation:false,
		autoHeight:false,
		switchTime:7000,
		duration:500,
		event:'click',
		number : '.number',
		items_count : '.items_count'
	},_options);

	return this.each(function(){
		var _this = jQuery(this);
		var _slides = jQuery(_options.slideElements, _this);
		var _pagerLinks = jQuery(_options.pagerLinks, _this);
		var _btnPrev = jQuery(_options.btnPrev, _this);
		var _btnNext = jQuery(_options.btnNext, _this);
		var _btnPlayPause = jQuery(_options.btnPlayPause, _this);
		var _pauseOnHover = _options.pauseOnHover;
		var _autoRotation = _options.autoRotation;
		var _activeClass = _options.activeClass;
		var _pausedClass = _options.pausedClass;
		var _playClass = _options.playClass;
		var _autoHeight = _options.autoHeight;
		var _duration = _options.duration;
		var _switchTime = _options.switchTime;
		var _controlEvent = _options.event;
		var _number = jQuery(_options.number, _this);
		var _items_count = jQuery(_options.items_count, _this);

		var _phase = true;
		var _hover = false;
		var _prevIndex = 0;
		var _currentIndex = 0;
		var _slideCount = _slides.length;
		var _timer;
		if(!_slideCount) return;
		_slides.hide().eq(_currentIndex).show();
		if(_autoRotation) _this.removeClass(_pausedClass).addClass(_playClass);
		else _this.removeClass(_playClass).addClass(_pausedClass);

		if(_btnPrev.length) {
			_btnPrev.bind(_controlEvent,function(){
				if (_phase) {
					prevSlide();
				}
				return false;
			});
		}
		if(_btnNext.length) {
			_btnNext.bind(_controlEvent,function(){
				if (_phase) {
					nextSlide();
				}
				return false;
			});
		}
		if(_pagerLinks.length) {
			_pagerLinks.each(function(_ind){
				jQuery(this).bind(_controlEvent,function(){
					if(_currentIndex != _ind) {
						_prevIndex = _currentIndex;
						_currentIndex = _ind;
						_phase = true;
						switchSlide();
					}
					return false;
				});
			});
		}

		if(_btnPlayPause.length) {
			_btnPlayPause.bind(_controlEvent,function(){
				if(_this.hasClass(_pausedClass)) {
					_this.removeClass(_pausedClass).addClass(_playClass);
					_autoRotation = true;
					autoSlide();
				} else {
					if(_timer) clearTimeout(_timer);
					_this.removeClass(_playClass).addClass(_pausedClass);
				}
				return false;
			});
		}

		function prevSlide() {
			_prevIndex = _currentIndex;
			if(_currentIndex > 0) _currentIndex--;
			else _currentIndex = _slideCount-1;
			switchSlide();
		}
		function nextSlide() {
			_prevIndex = _currentIndex;
			if(_currentIndex < _slideCount-1) _currentIndex++;
			else _currentIndex = 0;
			switchSlide();
		}
		function refreshStatus() {
			if(_pagerLinks.length) _pagerLinks.removeClass(_activeClass).eq(_currentIndex).addClass(_activeClass);
			_slides.eq(_prevIndex).removeClass(_activeClass);
			_slides.eq(_currentIndex).addClass(_activeClass);
			_number.text('Фотография '+(_currentIndex+1)+' из '+_slideCount);
			_items_count.text('('+_slideCount+')');
		}
		function switchSlide() {
			if (_phase) {
				_phase = false;
				_slides.eq(_prevIndex).fadeOut(_duration, function(){
					_slides.eq(_currentIndex).fadeIn(_duration, function(){
						_phase = true;
					});
				});
				
				//slide ********************************************************
				if (_slides.eq(_currentIndex).height()>0)
				$('.gallery-block .frame').animate({
						'height': _slides.eq(_currentIndex).height()
					},
					_duration
				);
				
				
				refreshStatus();
			}
			autoSlide();
		}

		function autoSlide() {
			if(!_autoRotation || _hover) return;
			if(_timer) clearTimeout(_timer);
			_timer = setTimeout(nextSlide,_switchTime+_duration);
		}
		if(_pauseOnHover) {
			_this.hover(function(){
				_hover = true;
				if(_timer) clearTimeout(_timer);
			},function(){
				_hover = false;
				autoSlide();
			});
		}
		refreshStatus();
		autoSlide();
	});
}