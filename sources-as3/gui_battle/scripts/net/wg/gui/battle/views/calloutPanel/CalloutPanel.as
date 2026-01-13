package net.wg.gui.battle.views.calloutPanel
{
   import flash.display.MovieClip;
   import net.wg.data.constants.InvalidationType;
   import net.wg.data.constants.generated.CROSSHAIR_VIEW_ID;
   import net.wg.gui.battle.views.calloutPanel.components.InteractionDynamicTextLabel;
   import net.wg.gui.battle.views.calloutPanel.components.VehicleInfoLabel;
   import net.wg.infrastructure.base.meta.ICalloutPanelMeta;
   import net.wg.infrastructure.base.meta.impl.CalloutPanelMeta;
   
   public class CalloutPanel extends CalloutPanelMeta implements ICalloutPanelMeta
   {
      
      private static const FADEIN_STATE_NAME:String = "fadeIn";
      
      private static const FADEOUT_STATE_NAME:String = "fadeOut";
      
      private static const TRIGGERED_FADEOUT_STATE_NAME:String = "fadeTriggered";
      
      private static const TRIGGERED_COMMENDATION_FADEOUT_STATE_NAME:String = "fadeTriggeredCommendation";
      
      private static const FADEOUT_ANIMATION_ENDFRAME:int = 83;
      
      private static const TRIGGERED_FADEOUT_ANIMATION_ENDFRAME:int = 67;
      
      private static const TRIGGERED_COMMENDATION_FADEOUT_ANIMATION_ENDFRAME:int = 127;
      
      private static const COMMENDATION_ACTION_NAME:String = "COMMENDATION";
      
      private static const STAGE_CENTER_OFFSET_X_DEFAULT:int = -136;
      
      private static const STAGE_CENTER_OFFSET_Y_DEFAULT:int = 14;
      
      private static const STAGE_CENTER_OFFSET_X_ARCADE:int = -186;
      
      private static const STAGE_CENTER_OFFSET_Y_ARCADE:int = 14;
      
      private static const STAGE_CENTER_OFFSET_X_SNIPER:int = -266;
      
      private static const STAGE_CENTER_OFFSET_Y_SNIPER:int = 94;
      
      private static const STAGE_CENTER_OFFSET_X_STRATEGIC:int = -166;
      
      private static const STAGE_CENTER_OFFSET_Y_STRATEGIC:int = 94;
       
      
      public var triggeredCalloutActionOverlay:MovieClip = null;
      
      public var triggeredCalloutAction:MovieClip = null;
      
      public var calloutActionOverlay:MovieClip = null;
      
      public var calloutAction:MovieClip = null;
      
      public var tankText:VehicleInfoLabel = null;
      
      public var interactionText:InteractionDynamicTextLabel = null;
      
      private var _hasShowData:Boolean = false;
      
      private var _hasHideData:Boolean = false;
      
      private var _wasAnswered:Boolean = false;
      
      private var _action:String = "";
      
      private var _stageWidth:Number = 0;
      
      private var _stageHeight:Number = 0;
      
      private var _crosshairType:uint = 0;
      
      public function CalloutPanel()
      {
         super();
         addFrameScript(FADEOUT_ANIMATION_ENDFRAME,this.onFadeOutAnimationCompleted);
         addFrameScript(TRIGGERED_FADEOUT_ANIMATION_ENDFRAME,this.onFadeOutAnimationCompleted);
         addFrameScript(TRIGGERED_COMMENDATION_FADEOUT_ANIMATION_ENDFRAME,this.onFadeOutAnimationCompleted);
         this.setCompVisible(false);
      }
      
      override protected function draw() : void
      {
         var _loc1_:int = 0;
         var _loc2_:int = 0;
         super.draw();
         if(isInvalid(InvalidationType.DATA))
         {
            this.tankText.updatePositionOnDraw();
            this.interactionText.updatePositionOnDraw();
         }
         if(isInvalid(InvalidationType.POSITION))
         {
            _loc1_ = this._stageWidth >> 1;
            _loc2_ = this._stageHeight >> 1;
            switch(this._crosshairType)
            {
               case CROSSHAIR_VIEW_ID.ARCADE:
                  _loc1_ += STAGE_CENTER_OFFSET_X_ARCADE;
                  _loc2_ += STAGE_CENTER_OFFSET_Y_ARCADE;
                  break;
               case CROSSHAIR_VIEW_ID.SNIPER:
                  _loc1_ += STAGE_CENTER_OFFSET_X_SNIPER;
                  _loc2_ += STAGE_CENTER_OFFSET_Y_SNIPER;
                  break;
               case CROSSHAIR_VIEW_ID.STRATEGIC:
                  _loc1_ += STAGE_CENTER_OFFSET_X_STRATEGIC;
                  _loc2_ += STAGE_CENTER_OFFSET_Y_STRATEGIC;
                  break;
               default:
                  _loc1_ += STAGE_CENTER_OFFSET_X_DEFAULT;
                  _loc2_ += STAGE_CENTER_OFFSET_Y_DEFAULT;
            }
            this.x = _loc1_;
            this.y = _loc2_;
         }
      }
      
      override protected function onDispose() : void
      {
         stop();
         addFrameScript(FADEOUT_ANIMATION_ENDFRAME,null);
         addFrameScript(TRIGGERED_FADEOUT_ANIMATION_ENDFRAME,null);
         addFrameScript(TRIGGERED_COMMENDATION_FADEOUT_ANIMATION_ENDFRAME,null);
         this.triggeredCalloutActionOverlay = null;
         this.triggeredCalloutAction = null;
         this.calloutActionOverlay = null;
         this.calloutAction = null;
         this.tankText.dispose();
         this.tankText = null;
         this.interactionText.dispose();
         this.interactionText = null;
         super.onDispose();
      }
      
      public function updateStage(param1:Number, param2:Number) : void
      {
         if(param1 == this._stageWidth && param2 == this._stageHeight)
         {
            return;
         }
         this._stageWidth = param1;
         this._stageHeight = param2;
         invalidatePosition();
      }
      
      override public function setCompVisible(param1:Boolean) : void
      {
         var _loc2_:String = null;
         if(param1 == _isCompVisible)
         {
            return;
         }
         if(param1 && this._hasShowData)
         {
            super.setCompVisible(param1);
            gotoAndPlay(FADEIN_STATE_NAME);
         }
         else if(!param1)
         {
            if(this._hasHideData)
            {
               onHideStartS();
               if(this._wasAnswered)
               {
                  _loc2_ = TRIGGERED_FADEOUT_STATE_NAME;
                  if(this._action == COMMENDATION_ACTION_NAME)
                  {
                     _loc2_ = TRIGGERED_COMMENDATION_FADEOUT_STATE_NAME;
                  }
                  gotoAndPlay(_loc2_);
               }
               else
               {
                  gotoAndPlay(FADEOUT_STATE_NAME);
               }
               this._hasHideData = false;
            }
            else
            {
               if(this._hasShowData)
               {
                  this.resetAndStopAnimation();
               }
               super.setCompVisible(param1);
            }
         }
      }
      
      public function as_setCrosshairType(param1:int) : void
      {
         if(param1 == this._crosshairType)
         {
            return;
         }
         this._crosshairType = param1;
         invalidatePosition();
      }
      
      public function as_setHideData(param1:Boolean, param2:String) : void
      {
         if(param1)
         {
            this.triggeredCalloutActionOverlay.gotoAndStop(param2);
            this.triggeredCalloutAction.gotoAndStop(param2);
         }
         this._hasHideData = true;
         this._wasAnswered = param1;
      }
      
      public function as_setData(param1:String, param2:String, param3:String, param4:String, param5:String, param6:String) : void
      {
         this._action = param1;
         this.calloutActionOverlay.gotoAndStop(param1);
         this.calloutAction.gotoAndStop(param1);
         this.tankText.setVehicleData(param2,param3);
         this.interactionText.setTextData(param4,param6,param5);
         invalidateData();
         this._hasShowData = true;
      }
      
      private function onFadeOutAnimationCompleted() : void
      {
         this.resetAndStopAnimation();
         this.setCompVisible(false);
      }
      
      private function resetAndStopAnimation() : void
      {
         this._hasShowData = false;
         this._hasHideData = false;
         this._wasAnswered = false;
         gotoAndStop(1);
         onHideCompletedS();
      }
   }
}
