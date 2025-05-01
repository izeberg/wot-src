package net.wg.historical_battles.gui.battle.views.gameMessagesPanel.components
{
   import flash.events.Event;
   import net.wg.gui.battle.views.gameMessagesPanel.components.EndGameMessage;
   import net.wg.infrastructure.managers.IStageSizeManager;
   import net.wg.utils.IStageSizeDependComponent;
   
   public class HBEndGameMessage extends EndGameMessage implements IStageSizeDependComponent
   {
       
      
      private var _textFields:HBEndGameMessageTextfields;
      
      private var _stageSizeMgr:IStageSizeManager;
      
      public function HBEndGameMessage()
      {
         this._stageSizeMgr = App.stageSizeMgr;
         super();
         this._textFields = HBEndGameMessageTextfields(textfields);
         addEventListener(Event.ADDED_TO_STAGE,this.onAddedToStageHandler,false,0,true);
         this._stageSizeMgr.register(this);
      }
      
      override protected function onDispose() : void
      {
         removeEventListener(Event.ADDED_TO_STAGE,this.onAddedToStageHandler,false);
         this._stageSizeMgr.unregister(this);
         this._stageSizeMgr = null;
         this._textFields = null;
         super.onDispose();
      }
      
      public function setStateSizeBoundaries(param1:int, param2:int) : void
      {
         this.updateLayout();
      }
      
      protected function updateLayout() : void
      {
         this._textFields.updateLayout(this._stageSizeMgr.currentBreakPoint);
      }
      
      private function onAddedToStageHandler(param1:Event) : void
      {
         this.updateLayout();
      }
   }
}
