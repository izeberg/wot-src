package net.wg.white_tiger.gui.battle.views.wtConsumablesPanel
{
   import flash.geom.ColorTransform;
   import net.wg.data.constants.InvalidationType;
   import net.wg.gui.battle.components.buttons.BattleToolTipButton;
   import net.wg.gui.battle.views.consumablesPanel.VO.ConsumablesVO;
   import net.wg.gui.components.controls.UILoaderAlt;
   import net.wg.white_tiger.gui.battle.views.wtConsumablesPanel.constants.WT_ABILITY_STATES;
   import net.wg.white_tiger.gui.battle.views.wtConsumablesPanel.interfaces.IWTBaseConsumablesButton;
   import org.idmedia.as3commons.util.StringUtils;
   
   public class BaseConsumablesButton extends BattleToolTipButton implements IWTBaseConsumablesButton
   {
      
      protected static const WT_STATE_VALIDATION:uint = InvalidationType.SYSTEM_FLAGS_BORDER << 2;
       
      
      public var iconLoader:UILoaderAlt = null;
      
      protected var wtState:String = null;
      
      private var _consumablesVO:ConsumablesVO = null;
      
      public function BaseConsumablesButton()
      {
         super();
         this._consumablesVO = new ConsumablesVO();
      }
      
      override protected function onDispose() : void
      {
         this.iconLoader.dispose();
         this.iconLoader = null;
         this._consumablesVO = null;
         super.onDispose();
      }
      
      override protected function draw() : void
      {
         super.draw();
         if(StringUtils.isNotEmpty(this.wtState) && isInvalid(WT_STATE_VALIDATION))
         {
            this.updateWtState();
         }
      }
      
      public function clearColorTransform() : void
      {
      }
      
      public function clearCoolDownTime() : void
      {
      }
      
      public function hideGlow() : void
      {
      }
      
      public function setBindKeyTextVisibility(param1:Boolean) : void
      {
      }
      
      public function setColorTransform(param1:ColorTransform) : void
      {
      }
      
      public function setCoolDownPosAsPercent(param1:Number) : void
      {
      }
      
      public function setCoolDownTime(param1:Number, param2:Number, param3:Number, param4:int = 1) : void
      {
      }
      
      public function setTimerSnapshot(param1:int, param2:Boolean) : void
      {
      }
      
      public function showGlow(param1:int) : void
      {
      }
      
      public function showGlowWithHotkey(param1:int, param2:Boolean = true) : void
      {
      }
      
      public function updateLevelInformation(param1:int) : void
      {
      }
      
      public function updateLockedInformation(param1:int, param2:String) : void
      {
      }
      
      public function wtSetDisabled(param1:Boolean) : void
      {
         var _loc2_:String = !!param1 ? WT_ABILITY_STATES.DISABLED : WT_ABILITY_STATES.DEFAULT;
         if(this.wtState != _loc2_)
         {
            this.wtState = _loc2_;
            invalidate(WT_STATE_VALIDATION);
         }
      }
      
      public function wtShowActive(param1:int) : void
      {
         if(this.wtState != WT_ABILITY_STATES.ACTIVE)
         {
            this.wtState = WT_ABILITY_STATES.ACTIVE;
            invalidate(WT_STATE_VALIDATION);
         }
      }
      
      protected function updateWtState() : void
      {
      }
      
      public function get bindSfKeyCode() : Number
      {
         return 0;
      }
      
      public function get consumablesVO() : ConsumablesVO
      {
         return this._consumablesVO;
      }
      
      public function set icon(param1:String) : void
      {
         this.iconLoader.source = param1;
      }
      
      public function set key(param1:Number) : void
      {
      }
      
      public function set quantity(param1:int) : void
      {
      }
      
      public function set activated(param1:Boolean) : void
      {
      }
      
      public function get showConsumableBorder() : Boolean
      {
         return false;
      }
      
      public function set showConsumableBorder(param1:Boolean) : void
      {
      }
      
      public function set isReplay(param1:Boolean) : void
      {
      }
   }
}
