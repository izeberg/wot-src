package net.wg.gui.battle.views.widgetsPanel
{
   import flash.display.BlendMode;
   import flash.display.DisplayObjectContainer;
   import flash.display.MovieClip;
   import net.wg.data.constants.generated.MECHANICS_WIDGET_CONST;
   import net.wg.infrastructure.base.meta.IAuxiliaryRocketLauncherWidgetMeta;
   import net.wg.infrastructure.base.meta.impl.AuxiliaryRocketLauncherWidgetMeta;
   
   public class AuxiliaryRocketLauncherWidget extends AuxiliaryRocketLauncherWidgetMeta implements IAuxiliaryRocketLauncherWidgetMeta
   {
      
      private static const UNDEPLOYING_STATE:String = "undeploying";
      
      private static const INSTANT_TRANSITION_STATES:Array = [MECHANICS_WIDGET_CONST.DISABLE];
       
      
      public var forwardProgress:MovieClip;
      
      public var hotkeyTarget:MovieClip = null;
      
      public var icon:MovieClip;
      
      public var flash:MovieClip;
      
      public function AuxiliaryRocketLauncherWidget()
      {
         super();
         blendMode = BlendMode.SCREEN;
      }
      
      override protected function applyState(param1:String, param2:Boolean) : void
      {
         var _loc3_:String = param1;
         if(this.state == MECHANICS_WIDGET_CONST.DEPLOYING && param1 == MECHANICS_WIDGET_CONST.READY)
         {
            _loc3_ = UNDEPLOYING_STATE;
         }
         super.applyState(_loc3_,param2);
         if(param2)
         {
            this.flash.gotoAndStop(_loc3_ + INSTANTLY_POSTFIX);
         }
         else if(_loc3_ == MECHANICS_WIDGET_CONST.ACTIVE || _loc3_ == MECHANICS_WIDGET_CONST.DEPLOYING || _loc3_ == UNDEPLOYING_STATE)
         {
            this.flash.gotoAndPlay(_loc3_);
         }
      }
      
      override protected function onDispose() : void
      {
         this.forwardProgress = null;
         this.hotkeyTarget = null;
         this.icon = null;
         this.flash = null;
         super.onDispose();
      }
      
      override protected function getHotKeysTarget() : DisplayObjectContainer
      {
         return this.hotkeyTarget;
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
         return _loc1_ && (this.state == MECHANICS_WIDGET_CONST.READY || this.state == MECHANICS_WIDGET_CONST.DEPLOYING);
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
