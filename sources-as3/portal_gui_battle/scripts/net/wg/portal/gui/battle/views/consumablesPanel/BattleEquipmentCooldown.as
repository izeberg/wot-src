package net.wg.portal.gui.battle.views.consumablesPanel
{
   import flash.display.MovieClip;
   import net.wg.gui.battle.components.BattleUIComponent;
   
   public class BattleEquipmentCooldown extends BattleUIComponent
   {
      
      private static const START_FRAME:int = 1;
       
      
      public var cooldownBar:MovieClip = null;
      
      public var activationBar:MovieClip = null;
      
      private var _currentBar:MovieClip = null;
      
      public function BattleEquipmentCooldown()
      {
         super();
         this._currentBar = this.cooldownBar;
      }
      
      override public function gotoAndStop(param1:Object, param2:String = null) : void
      {
         this._currentBar.gotoAndStop(param1,param2);
      }
      
      override protected function onDispose() : void
      {
         this.cooldownBar = null;
         this.activationBar = null;
         this._currentBar = null;
         super.onDispose();
      }
      
      public function useActivation() : void
      {
         this._currentBar.visible = false;
         this._currentBar = this.activationBar;
         this.gotoAndStop(START_FRAME);
         this._currentBar.visible = true;
      }
      
      public function useCooldown() : void
      {
         this._currentBar.visible = false;
         this._currentBar = this.cooldownBar;
         this.gotoAndStop(START_FRAME);
         this._currentBar.visible = true;
      }
   }
}
