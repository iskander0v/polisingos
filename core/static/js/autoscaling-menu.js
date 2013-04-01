$(function(){
	autoscalingMenu($('#nav ul'));
});
function autoscalingMenu(menu){
	var oldMenu = $(menu);
	var newMenu = $('<table cellspacing="0" cellpadding="0" class="UL"><tbody><tr></tr></tbody></table>');
	$('li', menu).each(function(){
		$('tr',newMenu).append($('<td class="LI">').append($(">*",this).clone()).addClass($(this).attr('class')));
	});
	$('td:first', newMenu).addClass('first');
	$('td:last', newMenu).addClass('last');
	newMenu.insertAfter(menu);
}
