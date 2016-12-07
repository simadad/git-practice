// Sauder features uses Z-indexes in the range of 10-30

function SauderFeatures(element, opt)
{
	if(typeof element == 'undefined') return this;

	// initialise the elements
	this.overlay			= null;
	this.element			= jQuery(element);
	this.id					= element.id;
	
	// initialise the variables
	this.nexti				= null;
	this.mouseover			= false;
	this.animatingpacket	= null;
	this.running			= false;
	this.counter			= 0;
	this.i					= 0;
	this.open				= 0;
	
	// initialise the settings
	this.delay				= opt.delay;
	this.auto				= opt.auto;
	this.tTime				= opt.tTime;
	this.tEasing			= opt.tEasing;
	
	// set up the listeners
	this._onInit				= opt.onInit;
	
	this.holder				= null;
	
	this.initialimage		= null;
	
	SauderFeatures.objects[this.id] = this;
	
	this.init();
}
SauderFeatures.objects = {};
SauderFeatures.getGalleryByName = function(name)
{
	return SauderFeatures.objects[name];
}
$pr = SauderFeatures.prototype;
$pr.isSauderFeatures	= true;
$pr.childSelector		= '.featureitem';
$pr.initClass			= 'SauderFeaturesInit';
$pr.subpositionClass	= 'subposition_';
$pr.openClass			= 'open';
$pr.childState			= {
							overflow: 'hidden',
							float: 'left',
							position: 'relative'
						  };
$pr.closedState			= {
							width: 55
						  };
$pr.openState			= {
							width: 780
						  };
						  
// getters and setters
$pr.setI = function(i)
{
	this.i = i;
}
$pr.getI = function()
{
	return parseInt(this.i);
}
$pr.getNext = function()
{
	var next = this.getI() + 1;
	
	if(next >= this.children.length)
	{
		next = 0;
	}
	
	return next;
}
$pr.getPrevious = function()
{
	var prev = this.getI() - 1;
	if(prev < 0)
	{
		prev = this.children.length - 1;
	}
	
	return prev;
}
$pr.setOpen = function(open)
{
	this.open = open;
}
$pr.getOpen = function()
{
	return this.open;
}
$pr.getIChild = function()
{
	return this.getChildByI(this.getI());
}
$pr.getOpenChild = function()
{
	return this.getChildByI(this.getOpen());
}
$pr.getChildByI = function(i)
{
	return jQuery(this.children[i]);
}
$pr.setIsAnimating = function(a)
{
	this.running = a == true;
}
$pr.isAnimating = function()
{
	return this.running == true;
}

// initialise
$pr.init = function()
{
	// intiialise the variables
	var p = this;
	var child;
	
	// remove titles
	jQuery('a',this.element).removeAttr('title');
	
	this.element.css({
	});
	
	// wrap the children
	this.element.wrapInner('<div class="lengthener"></div>');
	var lengthener = jQuery('div.lengthener',this.element);
	
	lengthener.css({
		width: 5000
	});
	lengthener.wrap('<div class="childwrapper"></div>');
	var wrapper = jQuery('div.childwrapper',wrapper);
	wrapper.css({
		width: 1000,
		height: 332,
		overflow: 'hidden'
	});
	
	// set up the overlay layer
	this.overlay = jQuery('<div></div>').appendTo(this.element);
	this.overlay.css({
		zIndex: 30,
		position: 'absolute',
		left: 0,
		top: 0,
		width: '100%',
		height: 1
	});

	// get the children
	this.children = jQuery(this.childSelector,this.element);
	
	// add the rollover
	this.element.hover(function(e)
	{
		p.onMouseIn(e);
	},
	function(e)
	{
		p.onMouseOut(e);
	}
	);
	this.children.mouseover(function(e)
	{
		p.onMouseOver(e);
	});

	for(var i=0; i < this.children.length; i++)
	{
		child = jQuery(this.children[i]);
		
		// set up the basic closed state
		child.css(this.childState);
		child.css(this.closedState);
		
		child.addClass('listpos_'+(i));
		
		// hide all children of children
		jQuery('> div',child).hide();
		
		// if we are the open item, open us up
		if(i == this.getOpen())
		{
			child.css(this.openState);
		}
	}
	
	var a = this.getChildByI(0);
	var apos = a.position();
	
	this.overlay.empty();
	
	// animate in any subcontent
	jQuery('> div', a).each(function(index)
	{
		var op = jQuery(this).clone().appendTo(p.overlay);
		op.show();
		var opos = op.position();
		
		var left = opos.left + apos.left;
		var top = opos.top;
		
		op.css({
			position: 'absolute',
			left: left,
			top: top - 100,
			bottom: 'auto',
			opacity: 0
		});
		op.delay(index * 200).animate({top: top, opacity: 1, 'filter': ''}, {duration: 200, easing: 'easeOutQuart'});
		
	});
	
	this.fixFeatures(0);
	
	// add our inited class to the element
	this.element.addClass(this.initClass);
	
	// start the timer up
	this.startTimer();
}
$pr.fixFeatures = function(mount)
{
	var op;
	var countdown = false;
	var z = 20;
	
	for(var i=0; i < this.children.length; i++)
	{
		op = jQuery(this.children[i]);
		
		if(i == mount)
		{
			op.css('zIndex', 10);
			countdown = true
		}
		
		if(countdown)
		{
			op.css('zIndex', z--);
		} else
		{
			op.css('zIndex', z++);
		}
	}
}

// timer functions
$pr.startTimer = function()
{
	var p = this;

	if(this.auto && !this.mouseover)
	{
		this.timer = setTimeout(function(){p.next()}, this.delay);
	}
}
$pr.clearTimer = function()
{
	clearTimeout(this.timer);
}

// process initialisation
$pr.next = function()
{
	var i = this.getNext();
	
	this.openByI(i);
}
$pr.previous = function()
{
	var i = this.getPrevious();
	
	this.openByI(i);
}
$pr.openByDiv = function(div)
{
	var opreg = new RegExp('listpos_([0-9]+)');
	var i = opreg.exec(div.attr('className'));
	
	if(typeof i == 'object' && i != null && i.length)
	{
		i = i[1];
	} else
	{
		return;
	}
	
	this.openByI(i);
	
	this.nexti = i;
}
$pr.openByNextI = function()
{
	if(this.nexti != null)
	{
		this.openByI(this.nexti);
	}
}
$pr.openByI = function(i)
{
	var openingChild, closingChild;
	
	if(i != this.getOpen() && i != this.getI() && !this.isAnimating())
	{
		// set the iterant
		this.setI(i);
		
		// stop any still running timer
		this.clearTimer();
		
		// start the transition
		this.startTransition();
	}
	
	this.nexti = null;
}
$pr.onMouseOver = function(e)
{
	var t = jQuery(e.target);
	var div = t.parents(this.childSelector);
	
	this.openByDiv(div);
	
	this.clearTimer();
}
$pr.hoverOver = function(e)
{
	var t = jQuery(e.target);
	
	this.mouseover = true;
	
	this.clearTimer();
}
$pr.hoverOut = function(e)
{
	var t = jQuery(e.target);
	
	this.mouseover = false;
	
	this.startTimer();
}

// running functions
$pr.startTransition = function()
{
	var p = this;
	// get the children that we need to manipulate
	var a = this.getIChild();
	var o = this.getOpenChild();
	// regexp for determining offset positions
	var opreg = new RegExp(this.subpositionClass+'([0-9]+)');
	var apos = opreg.exec(a.attr('className'));
	var opos = opreg.exec(o.attr('className'));

	// set the is animating switch
	this.setIsAnimating(true);
	
	this.animatingpacket = {};
	this.animatingpacket.aPosition = (typeof apos == 'object' && apos != null && apos.length) ? apos[1] : 0;
	this.animatingpacket.oPosition = (typeof opos == 'object' && opos != null && opos.length) ? opos[1] : 0;
	this.animatingpacket.aSub = jQuery('> a',a);
	this.animatingpacket.oSub = jQuery('> a',o);
	
	
	// set up the transition
//	o.animate(this.closedState, {duration: this.tTime, easing: this.tEasing});
		if(this.animatingpacket.oPosition > 0)
		{
			jQuery('> a',o).animate({left: - this.animatingpacket.oPosition}, {duration: this.tTime, easing: this.tEasing});
		}
	a.animate(this.openState, {duration: this.tTime, easing: this.tEasing, complete: function(){ p.onEnd(this) }, step: function(now, fx){ p.onStep(now, fx, this) } });
		if(this.animatingpacket.aPosition > 0)
		{
			jQuery('> a',a).animate({left: 0}, {duration: this.tTime, easing: this.tEasing});
		}
//	a.animate(this.openState, {duration: this.tTime, easing: this.tEasing, complete: function(){ p.onEnd(this) }, step: function(now, fx){ p.onStep(now, fx, this) } });
	
	// animate out any subcontent
	var sc = jQuery('> div', this.overlay);
	sc.addClass('transition');
	sc.animate({opacity:0}, {duration: 500, complete: function(){ jQuery(this).removeClass('transition'); }});
	
	// fix them
	this.fixFeatures(this.getI());
}
$pr.stepClose = function(feature, width, fx)
{
}
$pr.step = function(feature, width, fx)
{
//	var a = jQuery(feature)
	var o = this.getOpenChild();
	// this is too specific for here - work out a better way to do this.
	var oWidth = 780 - (width - 55);
//	var per = (width - 51) / (775 - 51) * 100;
	
//	this.animatingpacket.aSub.css('left', 0 - (this.animatingpacket.aPosition - (this.animatingpacket.aPosition / 100 * per)));
//	this.animatingpacket.oSub.css('left', 0 - (this.animatingpacket.oPosition / 100 * per));
	
	o.width(oWidth);
}
$pr.endTransition = function(a)
{
	var p = this;
	var o = this.getOpenChild();
	var a = jQuery(a);
	var apos = a.position();
	
	this.overlay.empty();
	
	// animate in any subcontent
	jQuery('> div', a).each(function(index)
	{
		var op = jQuery(this).clone().appendTo(p.overlay);
		op.show();
		var opos = op.position();
		var left = opos.left + apos.left;
		
		op.css({
			position: 'absolute',
			left: left,
			opacity: 0
		});
		jQuery('> div',op).children().css({
			opacity: 0
		});
		op.delay(index * 200).animate({opacity: 1, 'filter': ''}, {duration: 200, complete: function(){ jQuery('> div',this).children().animate({opacity: 1, 'filter': ''},{duration:200})}});
		
//		var opos = op.position();
//		
//		var left = opos.left + apos.left;
//		var top = opos.top;
//		
//		op.css({
//			position: 'absolute',
//			left: left,
//			top: top - 100,
//			bottom: 'auto',
//			opacity: 0
//		});
//		op.delay(index * 200).animate({top: top, opacity: 1}, {duration: 200, easing: 'easeOutQuart'});
		
	});
	jQuery('> div', o).stop(true, false).animate({opacity:0}, {duration: 50});
	
	this.children.removeClass(this.openClass);
	a.addClass(this.openClass);
	
	this.setOpen(this.getI());
	
	// reset our css to norms
	o.css(this.closedState);
	a.css(this.openState);
	
	// set the is animating switch
	this.setIsAnimating(false);
	
	// if we have a nexti in the queue
	if(this.nexti != null)
	{
		this.openByI(this.nexti);
		this.nexti = null;
		return;
	}
	
	// start the timer up
	this.startTimer();
}

// internal listeners
$pr.onStep = function(now, fx, feature)
{
	this.step(feature, now, fx);
}
$pr.onEnd = function(feature)
{
	this.endTransition(feature);
}
$pr.onMouseIn = function(e)
{
	this.hoverOver(e);
}
$pr.onMouseOut = function(e)
{
	this.hoverOut(e);
}

delete $pr;


	jQuery.fn.sauderFeatures = function(options)
	{
		this.each(function()
		{
			var settings =
			{
				delay:			4000,
				auto:			true,
				tTime:			362,
				tEasing:		'linear'
			};
			
			if(options)
			{
				jQuery.extend(settings, options);
			}
			
			var elements = jQuery(this).children();
		
			if (elements.length >= 1)
			{
				var feature = new SauderFeatures(jQuery(this),settings);
			}
		});
	};
	
	