package net.wg.white_tiger.gui.battle.views.helpers
{
   import scaleform.clik.motion.Tween;
   
   public interface IAnimateAlpha
   {
       
      
      function animateAlpha(param1:Number, param2:Number, param3:uint) : void;
      
      function onAlphaTweenComplete(param1:Tween) : void;
      
      function clearTweens() : void;
   }
}
