// Wrap in Suit jQuery
(function ($) {
    /*
        jQuery Autosize v1.16.5
        (c) 2013 Jack Moore - jacklmoore.com
        updated: 2013-02-11
        license: http://www.opensource.org/licenses/mit-license.php
    */
    (function(e){var t,o={className:"autosizejs",append:"",callback:!1},i="hidden",n="border-box",s="lineHeight",a='<textarea tabindex="-1" style="position:absolute; top:-999px; left:0; right:auto; bottom:auto; border:0; -moz-box-sizing:content-box; -webkit-box-sizing:content-box; box-sizing:content-box; word-wrap:break-word; height:0 !important; min-height:0 !important; overflow:hidden;"/>',r=["fontFamily","fontSize","fontWeight","fontStyle","letterSpacing","textTransform","wordSpacing","textIndent"],l="oninput",c="onpropertychange",h=e(a).data("autosize",!0)[0];h.style.lineHeight="99px","99px"===e(h).css(s)&&r.push(s),h.style.lineHeight="",e.fn.autosize=function(s){return s=e.extend({},o,s||{}),h.parentNode!==document.body&&e(document.body).append(h),this.each(function(){function o(){t=b,h.className=s.className,e.each(r,function(e,t){h.style[t]=f.css(t)})}function a(){var e,n,a;if(t!==b&&o(),!d){d=!0,h.value=b.value+s.append,h.style.overflowY=b.style.overflowY,a=parseInt(b.style.height,10),h.style.width=Math.max(f.width(),0)+"px",h.scrollTop=0,h.scrollTop=9e4,e=h.scrollTop;var r=parseInt(f.css("maxHeight"),10);r=r&&r>0?r:9e4,e>r?(e=r,n="scroll"):p>e&&(e=p),e+=g,b.style.overflowY=n||i,a!==e&&(b.style.height=e+"px",x&&s.callback.call(b)),setTimeout(function(){d=!1},1)}}var p,d,u,b=this,f=e(b),g=0,x=e.isFunction(s.callback);f.data("autosize")||((f.css("box-sizing")===n||f.css("-moz-box-sizing")===n||f.css("-webkit-box-sizing")===n)&&(g=f.outerHeight()-f.height()),p=Math.max(parseInt(f.css("minHeight"),10)-g,f.height()),u="none"===f.css("resize")||"vertical"===f.css("resize")?"none":"horizontal",f.css({overflow:i,overflowY:i,wordWrap:"break-word",resize:u}).data("autosize",!0),c in b?l in b?b[l]=b.onkeyup=a:b[c]=a:b[l]=a,e(window).resize(function(){d=!1,a()}),f.bind("autosize",function(){d=!1,a()}),a())})}})(window.jQuery||window.Zepto);

    /*
        Custom hook for Django Suit inlines
    */
    $(function () {
        Suit.after_inline.register('autosize_textarea', function (inline_prefix, row) {
            $(row).find('.autosize').autosize()
        });
    });
}(Suit.$));
