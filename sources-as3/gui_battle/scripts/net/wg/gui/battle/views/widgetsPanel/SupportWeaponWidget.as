package net.wg.gui.battle.views.widgetsPanel
{
   import flash.display.BlendMode;
   import flash.display.MovieClip;
   import net.wg.data.constants.generated.MECHANICS_WIDGET_CONST;
   import net.wg.infrastructure.base.meta.ISupportWeaponWidgetMeta;
   import net.wg.infrastructure.base.meta.impl.SupportWeaponWidgetMeta;
   
   public class SupportWeaponWidget extends SupportWeaponWidgetMeta implements ISupportWeaponWidgetMeta
   {
      
      private static const FLASH_ANIM_START_FRAME:int = 2;
      
      private static const INSTANT_TRANSITION_STATES:Array = [MECHANICS_WIDGET_CONST.DISABLE,MECHANICS_WIDGET_CONST.IDLE];
       
      
      public var forwardProgress:MovieClip;
      
      public var reverseProgress:MovieClip;
      
      public var icon:MovieClip;
      
      public var flash:MovieClip;
      
      public function SupportWeaponWidget()
      {
         super();
         blendMode = BlendMode.SCREEN;
      }
      
      override protected function applyState(param1:String, param2:Boolean) : void
      {
         super.applyState(param1,param2);
         if(param1 == MECHANICS_WIDGET_CONST.ACTIVE)
         {
            this.flash.gotoAndPlay(FLASH_ANIM_START_FRAME);
         }
      }
      
      override protected function onDispose() : void
      {
         this.forwardProgress = null;
         this.reverseProgress = null;
         this.icon = null;
         this.flash = null;
         super.onDispose();
      }
      
      override protected function getInitialState() : String
      {
         return MECHANICS_WIDGET_CONST.IDLE;
      }
      
      override protected function getInstantTransitionStates() : Array
      {
         return INSTANT_TRANSITION_STATES;
      }
      
      override protected function getHotKeyVisibility() : Boolean
      {
         var _loc1_:Boolean = super.getHotKeyVisibility();
         return _loc1_ && this.state == MECHANICS_WIDGET_CONST.READY;
      }
      
      public function as_setActiveProgress(param1:Number) : void
      {
         this.reverseProgress.gotoAndStop(WidgetsPanel.REVERES_PROGRESSION_MAX_FRAME * param1);
      }
      
      public function as_setPreparingProgress(param1:Number) : void
      {
         this.forwardProgress.gotoAndStop(WidgetsPanel.FORWARD_PROGRESSION_MAX_FRAME * param1);
      }
      
      public function as_shootDone() : void
      {
         this.icon.gotoAndPlay(1);
      }
   }
}
