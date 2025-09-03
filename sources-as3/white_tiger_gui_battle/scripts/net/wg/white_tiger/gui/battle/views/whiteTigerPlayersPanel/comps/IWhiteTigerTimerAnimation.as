package net.wg.white_tiger.gui.battle.views.whiteTigerPlayersPanel.comps
{
   import flash.events.IEventDispatcher;
   
   public interface IWhiteTigerTimerAnimation extends IEventDispatcher
   {
       
      
      function updateProgress(param1:Number, param2:int) : void;
   }
}
