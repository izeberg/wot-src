package net.wg.portal.gui.battle.views.consumablesPanel
{
   import net.wg.data.constants.generated.ANIMATION_TYPES;
   import net.wg.gui.battle.views.consumablesPanel.BattleEquipmentButton;
   import net.wg.gui.battle.views.consumablesPanel.constants.COLOR_STATES;
   
   public class BattleEquipmentButton extends net.wg.gui.battle.views.consumablesPanel.BattleEquipmentButton
   {
      
      private static const COOLDOWN_COUNTER_BG_RED:String = "red";
      
      private static const COOLDOWN_TEXT_COLOR:uint = 14718599;
      
      private static const NORMAL_TEXT_COLOR:uint = 12242378;
       
      
      private var _battleEquipmentCooldown:BattleEquipmentCooldown = null;
      
      public function BattleEquipmentButton()
      {
         super();
         this._battleEquipmentCooldown = cooldownMc as BattleEquipmentCooldown;
      }
      
      override public function setCoolDownTime(param1:Number, param2:Number, param3:Number, param4:int = 1) : void
      {
         super.setCoolDownTime(param1,param2,param3,param4);
         glow.setBindKeyTextVisibility(true);
         cooldownTimerTf.textColor = NORMAL_TEXT_COLOR;
         cooldownTimerTf.filters = [];
         this._battleEquipmentCooldown.transform.colorTransform = COLOR_STATES.NORMAL_COLOR_TRANSFORM;
         this._battleEquipmentCooldown.useActivation();
         if(param1 > 0)
         {
            if((param4 & ANIMATION_TYPES.MOVE_ORANGE_BAR_UP) > 0)
            {
               cooldownMc.transform.colorTransform = COLOR_STATES.ORANGE_COOLDOWN_COLOR_TRANSFORM;
               this._battleEquipmentCooldown.useCooldown();
               cooldownTimerTf.textColor = COOLDOWN_TEXT_COLOR;
               counterBg.gotoAndStop(COOLDOWN_COUNTER_BG_RED);
               glow.setBindKeyTextVisibility(false);
            }
            setColorTransform(COLOR_STATES.NORMAL_COLOR_TRANSFORM);
            iconLoader.transform.colorTransform = COLOR_STATES.NORMAL_COLOR_TRANSFORM;
         }
      }
   }
}
