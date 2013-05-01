$(document).ready(function(){
	
	/* call panel */
	$(".call-button").click(function(e) {          
		e.preventDefault();
		$(".call-panel").toggle();
		$(".call-button").toggleClass("call-open");
	});
	$(".call-panel").mouseup(function() {
		return false
	});
	$(document).mouseup(function(e) {
		if($(e.target).parent(".call-button").length==0) {
			$(".call-button").removeClass("call-open");
			$(".call-panel").hide();
		}
	});
	
	/* tab */
	$(function(){$('.tabs').delegate('li:not(.active)','click',function(){$(this).addClass('active').siblings().removeClass('active').parents('#tab').find('.box').hide().eq($(this).index()).fadeIn(250);})});

	/* checkbox-mod */
	$('.mod-checkbox').formReplacer();
	
	/* select */
	$(".select").selectbox();
	 
    
});//document ready

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        function getCookie(name) {
            var cookieValue = null;
            if (document.cookie && document.cookie != '') {
                var cookies = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = jQuery.trim(cookies[i]);
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) == (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }
        if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
            // Only send the token to relative URLs i.e. locally.
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
            xhr.setRequestHeader("Content-Type", 'application/x-www-form-urlencoded; charset=UTF-8');

        }
    }
});

//formReplacer.min.js
(function (b) {
    b.fn.formReplacer = function (x) {
        function s(a) {
            a.which = a.which || a.keyCode;
            if (a.which === 32) {
                b(this).click();
                return false
            }
        }
        function l(a, d, c) {
            var e;
            a.each(function () {
                e = d ? !b(this).hasClass("selected") : c;
                b(this).toggleClass("selected", e);
                b(':checkbox[name="' + b(this).data("name") + '"][value="' + b(this).data("value") + '"]').attr("checked", e)
            })
        }
        function t(a) {
            a.newObj = b('<span class="modify' + a.className + " " + a.existingClasses + '" id="' + a.existingIDs + '" tabindex="' + n(a.old) + '"><span></span></span>');
            a.elemImgObj = b('<span class="modify' + a.className + 'Img"></span>');
            a.newObj.data("name", a.nameAttr);
            a.newObj.data("value", a.old.attr("value"));
            a.newObj.data("disabled", a.old.is(":disabled"));
            a.newObj.toggleClass("selected", a.old.is(":checked"));
            a.newObj.toggleClass("disabled", a.newObj.data("disabled"));
            a.old.after(a.newObj);
            a.newObj.append(a.elemImgObj).append(a.label)
        }
        function u(a) {
            b(a.target).parents(".modifySelectOptions").length || b(".modifySelectOptions").slideUp(100)
        }
        function v() {
            if (b.browser.msie) document.selection.empty();
            else b.browser.opera && parseInt(b.browser.version, 10) === 9 || window.getSelection().removeAllRanges()
        }
        function o(a) {
            var d = a.shiftKey || a.ctrlKey;
            d && v();
            this.onselectstart = function () {
                return !d
            };
            return !d
        }
        function w(a) {
            a.which = a.which || a.keyCode;
            if (a.which === 32 || a.which === i.up || a.which === i.down || a.which === i.right || a.which === i.left) return false
        }
        function j(a) {
            a.css("outline", "none").data("outlined", false)
        }
        function y(a) {
            a.css("outline", "none");
            a.focusout(function () {
                b(this).css("outline", "none")
            });
            a.keyup(function (d) {
                d.which = d.which || d.keyCode;
                d.which === 9 && b(this).css("outline", "#fff dotted thin")
            })
        }
        function n(a) {
            m.tabIndex = a.attr("tabindex") ? a.attr("tabindex") : ++m.prevTabIndex;
            return m.prevTabIndex = m.tabIndex
        }
        function p(a, d) {
            a.each(function () {
                if (d.children('option[value="' + a.data("value") + '"]').attr("selected") === true) {
                    a.removeClass("selected");
                    d.children('option[value="' + a.data("value") + '"]').attr("selected", false)
                } else {
                    a.addClass("selected");
                    d.children('option[value="' + a.data("value") + '"]').attr("selected", true)
                }
            })
        }
        var z = b.extend({
            rtl: false
        }, x),
            m = {
                tabIndex: 0,
                prevTabIndex: 0
            },
            h = {
                lastClicked: {},
                checkAll: true
            },
            i = {
                left: 37,
                up: 38,
                right: 39,
                down: 40
            },
            r = {
                radio: {
                    create: t,
                    events: {
                        click: function (a) {
                            a.preventDefault();
                            b(".modifyRadio").filter(function () {
                                return b(this).data("name") === a.data.obj.newObj.data("name")
                            }).removeClass("selected");
                            b(':radio[name="' + a.data.obj.newObj.data("name") + '"]').each(function () {
                                b(this).attr("checked", false)
                            });
                            a.data.obj.old.filter('[value="' + a.data.obj.newObj.data("value") + '"]').attr("checked", true);
                            a.data.obj.newObj.addClass("selected")
                        },
                        keypress: s
                    }
                },
                checkbox: {
                    create: t,
                    events: {
                        click: function (a) {
                            a.preventDefault();
                            j(b(this));
                            var d = b(".modifyCheckbox").filter(function () {
                                return b(this).data("name") === a.data.obj.nameAttr && !b(this).data("disabled")
                            }),
                                c = d.index(b(this));
                            h.lastClicked[a.data.obj.nameAttr] || (h.lastClicked[a.data.obj.nameAttr] = null);
                            if (a.shiftKey) if (h.lastClicked[a.data.obj.nameAttr] === null) {
                                l(d.filter(":lt(" + c + ")").andSelf(), false, true);
                                l(d.filter(":gt(" + c + ")"), false, false)
                            } else {
                                var e = d.index(h.lastClicked[a.data.obj.nameAttr]);
                                c = d.slice(e <= c ? e : c, e <= c ? c + 1 : e + 1);
                                l(c, false, true);
                                l(d.not(c), false, false)
                            } else {
                                h.lastClicked[a.data.obj.nameAttr] = b(this);
                                l(b(this), true, false)
                            }
                        },
                        mousedown: o,
                        keypress: s
                    }
                },
                "select-one": {
                    create: function (a) {
                        a.newObj = b('<span class="modifySelect ' + a.existingClasses + '" id="' + a.existingIDs + '" tabindex="' + n(a.old) + '"></span>');

                        a.options = a.old.children("option");
                        a.hasOptGroups = !! a.old.has("optgroup").length;
                        a.optGroups = a.hasOptGroups ? a.old.children("optgroup") : null;
                        a.currentOption = a.hasOptGroups ? a.old.find("option:selected").text() : a.options.filter(":selected").text();
                        a.newOptions = b('<ul class="modifySelectOptions"></ul>').hide();
                        a.newObj.data("name", a.nameAttr);
                        a.newOptions.data("name", a.nameAttr);
                        a.newObj.data("disabled", a.old.is(":disabled"));
                        a.newObj.toggleClass("disabled", a.newObj.data("disabled"));
                        if (!a.newObj.data("disabled")) {
                            b(document).unbind("click", u);
                            b(document).bind("click", {
                                obj: a
                            }, u);
                            a.newOptions.delegate("li", "click", function (d) {
                                if (!b(d.target).hasClass("modifyOptGroup") && !b(d.target).data("disabled")) {
                                    a.newOptions.slideUp(100);
                                    a.newObj.html("<span class='modifySelectBg'>" + b(this).text() + "</span>");
                                    a.old.val(b(this).data("value"))
                                }
                            })
                        }
                        a.hasOptGroups ? a.optGroups.each(function () {
                            var d = b('<li id="' + b(this).attr("id") + '" class="modifyOptGroup ' + b(this).attr("class") + '">' + b(this).attr("label") + "</li>");
                            a.newOptions.append(d);
                            b(this).children("option").each(function (c, e) {
                                var g = b(e).text() !== "" ? b(e).text() : "&nbsp;",
                                    q = b(e).attr("class"),
                                    A = b(e).is(":disabled") ? "disabled" : "";
                                g = b("<li/>", {
                                    "class": q + " " + A,
                                    id: b(e).attr("id"),
                                    text: g
                                }).data("value", b(e).val()).data("disabled", b(e).is(":disabled"));
                                a.newOptions.append(g)
                            })
                        }) : a.options.each(function (d, c) {
                            var e = b(c).text() !== "" ? b(c).text() : "&nbsp;",
                                g = b(c).attr("class"),
                                q = b(c).is(":disabled") ? "disabled" : "";
                            e = b("<li/>", {
                                "class": g + " " + q,
                                id: b(c).attr("id"),
                                text: e
                            }).data("value", b(c).val()).data("disabled", b(c).is(":disabled"));
                            a.newOptions.append(e)
                        });
                        jQuery.browser.msie && parseInt(jQuery.browser.version, 10) <= 6 && a.newOptions.children("li").css("width", a.newOptions.width());
                        a.newObj.html(a.currentOption !== "" ? a.currentOption : "&nbsp;").insertAfter(a.old).after(a.newOptions)
                    },
                    events: {
                        click: function (a) {
                            a.stopPropagation();
                            j(b(this));
                            a.data.obj.newOptions.css({
                                position: "absolute",
                                top: a.data.obj.newObj.offset().top + a.data.obj.newObj.outerHeight(),
                                left: z.rtl ? a.data.obj.newObj.offset().left + a.data.obj.newObj.outerWidth() - a.data.obj.newOptions.outerWidth() : a.data.obj.newObj.offset().left,
                                zIndex: "9999"
                            });
                            a.data.obj.newOptions.slideToggle(100)
                        },
                        keydown: function (a) {
                            var d = a.data.obj.newOptions.children(),
                                c = d.length,
                                e = d.filter(function () {
                                    return b(this).data("value") === a.data.obj.old.val()
                                });
                            a.which = a.which || a.keyCode;
                            if (a.which === i.right || a.which === i.down) {
                                var g = e.next();
                                if (d.index(e) + 1 !== c) {
                                    for (; g.data("disabled") || g.hasClass("modifyOptGroup");) g = g.next();
                                    g.click()
                                }
                                return false
                            } else if (a.which === i.left || a.which === i.up) {
                                c = e.prev();
                                if (d.index(e) !== 0) {
                                    for (; c.data("disabled") || c.hasClass("modifyOptGroup");) c = c.prev();
                                    c.click()
                                }
                                return false
                            }
                        },
                        keypress: w
                    }
                },
                "select-multiple": {
                    create: function (a) {
                        a.newObj = b('<ul id="' + a.existingIDs + '" class="modifySelectMultiple ' + a.existingClasses + '" tabindex="' + n(a.old) + '"></ul>').data("name", a.old.attr("name"));
                        a.newObj.data("disabled", a.old.is(":disabled"));
                        a.newObj.toggleClass("disabled", a.newObj.data("disabled"));
                        a.options = a.old.children("option");
                        a.selectedOptions = a.old.children("option:selected");
                        a.lastClicked = null;
                        a.options.each(function (d, c) {
                            var e = b(c).text() !== "" ? b(c).text() : "&nbsp;";
                            e = b("<li/>", {
                                "class": b(c).attr("class"),
                                id: b(c).attr("id"),
                                text: e
                            }).data("value", b(c).val()).data("disabled", b(c).is(":disabled"));
                            e.toggleClass("selected", b(c).is(":selected"));
                            e.toggleClass("disabled", e.data("disabled"));
                            a.newObj.append(e)
                        });
                        a.newObj.data("disabled") || a.newObj.delegate("li", "click", function (d) {
                            if (!b(d.target).data("disabled")) {
                                j(a.newObj);
                                if (d.shiftKey) if (a.lastClicked === null) {
                                    a.old.children('option[value="' + b(this).data("value") + '"]').prevAll().andSelf().filter(function () {
                                        return b(this).attr("disabled") === false
                                    }).attr("selected", true);
                                    b(this).prevAll().andSelf().filter(function () {
                                        return b(this).data("disabled") === false
                                    }).addClass("selected");
                                    a.old.children('option[value="' + b(this).data("value") + '"]').nextAll().attr("selected", false);
                                    b(this).nextAll().removeClass("selected")
                                } else {
                                    d = a.lastClicked.index() <= b(this).index() ? a.lastClicked.index() : b(this).index();
                                    var c = a.lastClicked.index() <= b(this).index() ? b(this).index() + 1 : a.lastClicked.index() + 1,
                                        e = b(this).siblings().andSelf().slice(d, c);
                                    d = a.old.children("option").slice(d, c);
                                    d.filter(function () {
                                        return b(this).attr("disabled") === false
                                    }).attr("selected", true);
                                    e.filter(function () {
                                        return b(this).data("disabled") === false
                                    }).addClass("selected");
                                    a.old.children("option").not(d).attr("selected", false);
                                    b(this).siblings().not(e).removeClass("selected")
                                } else {
                                    a.lastClicked = b(this);
                                    e = a.old.children('option[value="' + b(this).data("value") + '"]');
                                    if (d.ctrlKey) {
                                        d = e.is(":selected");
                                        e.attr("selected", !d);
                                        b(this).toggleClass("selected", !d)
                                    } else {
                                        e.attr("selected", true);
                                        b(this).addClass("selected");
                                        e.siblings().attr("selected", false);
                                        b(this).siblings().removeClass("selected")
                                    }
                                }
                            }
                        });
                        a.newObj.insertAfter(a.old);
                        a.newObj.css("width", a.newObj.width() + 20)
                    },
                    events: {
                        mousedown: o,
                        keypress: w,
                        focus: o,
                        keydown: function (a) {
                            v();
                            a.which = a.which || a.keyCode;
                            var d = b.Event("click"),
                                c = b(this).children("li").filter(function () {
                                    return a.data.obj.old.children('option[value="' + b(this).data("value") + '"]').is(":selected")
                                });
                            d.shiftKey = true;
                            if (a.which === 32) {
                                p(b(this).children("li").filter(function () {
                                    return b(this).data("outlined") === true
                                }), a.data.obj.old);
                                return false
                            }
                            if (a.which === i.right || a.which === i.down) {
                                for (var e = c.length === 0 ? b(this).children("li:first") : c.filter(":last").next(); e.data("disabled");) e = e.next();
                                if (a.shiftKey) {
                                    k > 0 ? p(c.filter(":first"), a.data.obj.old) : e.trigger(d);
                                    c.filter(b(this).children("li:not(.disabled):last")).length || k--
                                } else if (a.ctrlKey) {
                                    j(b(this).children("li"));
                                    if (f === null) f = 0;
                                    b(this).children("li:not(.disabled)").eq(f).data("outlined", true).css("outline", "#fff dotted thin");
                                    f = f < b(this).children("li:not(.disabled)").length - 1 ? ++f : f
                                } else {
                                    j(b(this).children("li"));
                                    k = 0;
                                    if (b(this).children("li:not(.disabled)").index(c.filter(":last")) !== b(this).children("li:not(.disabled)").length - 1) {
                                        e.click();
                                        f = b(this).children("li:not(.disabled)").index(e)
                                    } else {
                                        b(this).children("li:not(.disabled):last").click();
                                        f = b(this).children("li:not(.disabled)").length - 1
                                    }
                                }
                                return false
                            } else if (a.which === i.left || a.which === i.up) {
                                for (e = c.length === 0 ? b(this).children("li:first") : c.filter(":first").prev(); e.data("disabled");) e = e.prev();
                                if (a.shiftKey) {
                                    k < 0 ? p(c.filter(":last"), a.data.obj.old) : e.trigger(d);
                                    c.filter(b(this).children("li:not(.disabled):first")).length || k++
                                } else if (a.ctrlKey) {
                                    k++;
                                    f = f > 0 ? --f : f;
                                    j(b(this).children("li"));
                                    b(this).children("li:not(.disabled)").eq(f).data("outlined", true).css("outline", "#fff dotted thin")
                                } else {
                                    j(b(this).children("li"));
                                    k = 0;
                                    if (b(this).children("li:not(.disabled)").index(c.filter(":first")) !== 0) {
                                        e.click();
                                        f = b(this).children("li:not(.disabled)").index(e)
                                    } else {
                                        b(this).children("li:not(.disabled):first").click();
                                        f = b(this).children("li:not(.disabled)").index("li:not(.disabled):first")
                                    }
                                }
                                return false
                            }
                        }
                    }
                }
            },
            k = 0,
            f = null,
            B = function () {
                var a = function (d, c) {
                        this.className = d.replace(/^./, d.match(/^./)[0].toUpperCase());
                        this.elemType = d;
                        this.old = b(c).hide();
                        this.existingClasses = b(c).attr("class");
                        this.existingIDs = b(c).attr("id");
                        this.nameAttr = b(this.old).attr("name");
                        this.label = b('label[for="' + b(this.old).attr("id") + '"]');
                        r[this.elemType].create(this);
                        this.newObj.data("disabled") || this.newObj.bind(r[this.elemType].events, {
                            obj: this
                        })
                    };
                return function (d, c) {
                    return new a(d, c)
                }
            }();
        this.each(function () {
            if (this.type in r) {
                var a = new B(this.type, this);
                y(a.newObj)
            }
        });
        b(".checkAll").click(function () {
            var a = b(this).attr("class").replace(/(checkAll\s)(.*)/, "$2").split(" "),
                d = 0,
                c = 0,
                e = null,
                g;
            for (g in a) {
                e = b(".modifyCheckbox").filter(function () {
                    return b(this).data("name") === a[g]
                });
                e.each(function () {
                    d++;
                    b(':checkbox[value="' + b(this).data("value") + '"]').is(":checked") && c++
                });
                if (d == c && h.checkAll) h.checkAll = false;
                if (c === 0 && !h.checkAll) h.checkAll = true;
                e.each(function () {
                    b(this).toggleClass("selected", h.checkAll);
                    b(':checkbox[value="' + b(this).data("value") + '"]').attr("checked", h.checkAll)
                })
            }
            h.checkAll = !h.checkAll;
            return false
        });
        return this
    }
})(jQuery);


/* selectbox plugin 0.2 */
(function($,undefined){var PROP_NAME="selectbox",FALSE=false,TRUE=true;function Selectbox(){this._state=[];this._defaults={classHolder:"sbHolder",classHolderDisabled:"sbHolderDisabled",classSelector:"sbSelector",classOptions:"sbOptions",classGroup:"sbGroup",classSub:"sbSub",classDisabled:"sbDisabled",classToggleOpen:"sbToggleOpen",classToggle:"sbToggle",classFocus:"sbFocus",speed:200,effect:"fade",onChange:null,onOpen:null,onClose:null}}$.extend(Selectbox.prototype,{_isOpenSelectbox:function(target){if(!target){return FALSE}var inst=this._getInst(target);return inst.isOpen},_isDisabledSelectbox:function(target){if(!target){return FALSE}var inst=this._getInst(target);return inst.isDisabled},_attachSelectbox:function(target,settings){if(this._getInst(target)){return FALSE}var $target=$(target),self=this,inst=self._newInst($target),sbHolder,sbSelector,sbToggle,sbOptions,s=FALSE,optGroup=$target.find("optgroup"),opts=$target.find("option"),olen=opts.length;$target.attr("sb",inst.uid);$.extend(inst.settings,self._defaults,settings);self._state[inst.uid]=FALSE;$target.hide();function closeOthers(){var key,sel,uid=this.attr("id").split("_")[1];for(key in self._state){if(key!==uid){if(self._state.hasOwnProperty(key)){sel=$("select[sb='"+key+"']")[0];if(sel){self._closeSelectbox(sel)}}}}}sbHolder=$("<div>",{id:"sbHolder_"+inst.uid,"class":inst.settings.classHolder,tabindex:$target.attr("tabindex")});sbSelector=$("<a>",{id:"sbSelector_"+inst.uid,href:"#","class":inst.settings.classSelector,click:function(e){e.preventDefault();closeOthers.apply($(this),[]);var uid=$(this).attr("id").split("_")[1];if(self._state[uid]){self._closeSelectbox(target)}else{self._openSelectbox(target)}}});sbToggle=$("<a>",{id:"sbToggle_"+inst.uid,href:"#","class":inst.settings.classToggle,click:function(e){e.preventDefault();closeOthers.apply($(this),[]);var uid=$(this).attr("id").split("_")[1];if(self._state[uid]){self._closeSelectbox(target)}else{self._openSelectbox(target)}}});sbToggle.appendTo(sbHolder);sbOptions=$("<ul>",{id:"sbOptions_"+inst.uid,"class":inst.settings.classOptions,css:{display:"none"}});$target.children().each(function(i){var that=$(this),li,config={};if(that.is("option")){getOptions(that)}else{if(that.is("optgroup")){li=$("<li>");$("<span>",{text:that.attr("label")}).addClass(inst.settings.classGroup).appendTo(li);li.appendTo(sbOptions);if(that.is(":disabled")){config.disabled=true}config.sub=true;getOptions(that.find("option"),config)}}});function getOptions(){var sub=arguments[1]&&arguments[1].sub?true:false,disabled=arguments[1]&&arguments[1].disabled?true:false;arguments[0].each(function(i){var that=$(this),li=$("<li>"),child;if(that.is(":selected")){sbSelector.text(that.text());s=TRUE}if(i===olen-1){li.addClass("last")}if(!that.is(":disabled")&&!disabled){child=$("<a>",{href:"#"+that.val(),rel:that.val()}).text(that.text()).bind("click.sb",function(e){if(e&&e.preventDefault){e.preventDefault()}var t=sbToggle,$this=$(this),uid=t.attr("id").split("_")[1];self._changeSelectbox(target,$this.attr("rel"),$this.text());self._closeSelectbox(target)}).bind("mouseover.sb",function(){var $this=$(this);$this.parent().siblings().find("a").removeClass(inst.settings.classFocus);$this.addClass(inst.settings.classFocus)}).bind("mouseout.sb",function(){$(this).removeClass(inst.settings.classFocus)});if(sub){child.addClass(inst.settings.classSub)}if(that.is(":selected")){child.addClass(inst.settings.classFocus)}child.appendTo(li)}else{child=$("<span>",{text:that.text()}).addClass(inst.settings.classDisabled);if(sub){child.addClass(inst.settings.classSub)}child.appendTo(li)}li.appendTo(sbOptions)})}if(!s){sbSelector.text(opts.first().text())}$.data(target,PROP_NAME,inst);sbHolder.data("uid",inst.uid).bind("keydown.sb",function(e){var key=e.charCode?e.charCode:e.keyCode?e.keyCode:0,$this=$(this),uid=$this.data("uid"),inst=$this.siblings("select[sb='"+uid+"']").data(PROP_NAME),trgt=$this.siblings(["select[sb='",uid,"']"].join("")).get(0),$f=$this.find("ul").find("a."+inst.settings.classFocus);switch(key){case 37:case 38:if($f.length>0){var $next;$("a",$this).removeClass(inst.settings.classFocus);$next=$f.parent().prevAll("li:has(a)").eq(0).find("a");if($next.length>0){$next.addClass(inst.settings.classFocus).focus();$("#sbSelector_"+uid).text($next.text())}}break;case 39:case 40:var $next;$("a",$this).removeClass(inst.settings.classFocus);if($f.length>0){$next=$f.parent().nextAll("li:has(a)").eq(0).find("a")}else{$next=$this.find("ul").find("a").eq(0)}if($next.length>0){$next.addClass(inst.settings.classFocus).focus();$("#sbSelector_"+uid).text($next.text())}break;case 13:if($f.length>0){self._changeSelectbox(trgt,$f.attr("rel"),$f.text())}self._closeSelectbox(trgt);break;case 9:if(trgt){var inst=self._getInst(trgt);if(inst){if($f.length>0){self._changeSelectbox(trgt,$f.attr("rel"),$f.text())}self._closeSelectbox(trgt)}}var i=parseInt($this.attr("tabindex"),10);if(!e.shiftKey){i++}else{i--}$("*[tabindex='"+i+"']").focus();break;case 27:self._closeSelectbox(trgt);break}e.stopPropagation();return false}).delegate("a","mouseover",function(e){$(this).addClass(inst.settings.classFocus)}).delegate("a","mouseout",function(e){$(this).removeClass(inst.settings.classFocus)});sbSelector.appendTo(sbHolder);sbOptions.appendTo(sbHolder);sbHolder.insertAfter($target);$("html").live("mousedown",function(e){e.stopPropagation();$("select").selectbox("close")});$([".",inst.settings.classHolder,", .",inst.settings.classSelector].join("")).mousedown(function(e){e.stopPropagation()})},_detachSelectbox:function(target){var inst=this._getInst(target);if(!inst){return FALSE}$("#sbHolder_"+inst.uid).remove();$.data(target,PROP_NAME,null);$(target).show()},_changeSelectbox:function(target,value,text){var onChange,inst=this._getInst(target);if(inst){onChange=this._get(inst,"onChange");$("#sbSelector_"+inst.uid).text(text)}value=value.replace(/\'/g,"\\'");$(target).find("option[value='"+value+"']").attr("selected",TRUE);if(inst&&onChange){onChange.apply((inst.input?inst.input[0]:null),[value,inst])}else{if(inst&&inst.input){inst.input.trigger("change")}}},_enableSelectbox:function(target){var inst=this._getInst(target);if(!inst||!inst.isDisabled){return FALSE}$("#sbHolder_"+inst.uid).removeClass(inst.settings.classHolderDisabled);inst.isDisabled=FALSE;$.data(target,PROP_NAME,inst)},_disableSelectbox:function(target){var inst=this._getInst(target);if(!inst||inst.isDisabled){return FALSE}$("#sbHolder_"+inst.uid).addClass(inst.settings.classHolderDisabled);inst.isDisabled=TRUE;$.data(target,PROP_NAME,inst)},_optionSelectbox:function(target,name,value){var inst=this._getInst(target);if(!inst){return FALSE}inst[name]=value;$.data(target,PROP_NAME,inst)},_openSelectbox:function(target){var inst=this._getInst(target);if(!inst||inst.isOpen||inst.isDisabled){return }var el=$("#sbOptions_"+inst.uid),viewportHeight=parseInt($(window).height(),10),offset=$("#sbHolder_"+inst.uid).offset(),scrollTop=$(window).scrollTop(),height=el.prev().height(),diff=viewportHeight-(offset.top-scrollTop)-height/2,onOpen=this._get(inst,"onOpen");el.css({top:height+"px",maxHeight:(diff-height)+"px"});inst.settings.effect==="fade"?el.fadeIn(inst.settings.speed):el.slideDown(inst.settings.speed);$("#sbToggle_"+inst.uid).addClass(inst.settings.classToggleOpen);this._state[inst.uid]=TRUE;inst.isOpen=TRUE;if(onOpen){onOpen.apply((inst.input?inst.input[0]:null),[inst])}$.data(target,PROP_NAME,inst)},_closeSelectbox:function(target){var inst=this._getInst(target);if(!inst||!inst.isOpen){return }var onClose=this._get(inst,"onClose");inst.settings.effect==="fade"?$("#sbOptions_"+inst.uid).fadeOut(inst.settings.speed):$("#sbOptions_"+inst.uid).slideUp(inst.settings.speed);$("#sbToggle_"+inst.uid).removeClass(inst.settings.classToggleOpen);this._state[inst.uid]=FALSE;inst.isOpen=FALSE;if(onClose){onClose.apply((inst.input?inst.input[0]:null),[inst])}$.data(target,PROP_NAME,inst)},_newInst:function(target){var id=target[0].id.replace(/([^A-Za-z0-9_-])/g,"\\\\$1");return{id:id,input:target,uid:Math.floor(Math.random()*99999999),isOpen:FALSE,isDisabled:FALSE,settings:{}}},_getInst:function(target){try{return $.data(target,PROP_NAME)}catch(err){throw"Missing instance data for this selectbox"}},_get:function(inst,name){return inst.settings[name]!==undefined?inst.settings[name]:this._defaults[name]}});$.fn.selectbox=function(options){var otherArgs=Array.prototype.slice.call(arguments,1);if(typeof options=="string"&&options=="isDisabled"){return $.selectbox["_"+options+"Selectbox"].apply($.selectbox,[this[0]].concat(otherArgs))}if(options=="option"&&arguments.length==2&&typeof arguments[1]=="string"){return $.selectbox["_"+options+"Selectbox"].apply($.selectbox,[this[0]].concat(otherArgs))}return this.each(function(){typeof options=="string"?$.selectbox["_"+options+"Selectbox"].apply($.selectbox,[this].concat(otherArgs)):$.selectbox._attachSelectbox(this,options)})};$.selectbox=new Selectbox();$.selectbox.version="0.2"})(jQuery);