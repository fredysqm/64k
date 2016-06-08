(function ($, undefined) {
    $.ajaxSetup({
        beforeSend:function (xhr, settings) {
            if (settings.context != undefined && settings.context.hasClass('btn')) {
                settings.context.button('loading');
            }
        },
        complete:function () {
            this.button('reset');
        }
    });
})(jQuery);