package net.wg.gui.lobby.tank_setup
{
   import fl.transitions.easing.Regular;
   import flash.display.Stage;
   import flash.events.Event;
   import flash.events.KeyboardEvent;
   import flash.ui.Keyboard;
   import net.wg.data.constants.generated.HANGAR_ALIASES;
   import net.wg.gui.lobby.hangar.HangarAmunitionSwitchAnimator;
   import net.wg.gui.lobby.hangar.VehicleParametersWithHighlight;
   import net.wg.infrastructure.base.meta.IAmmunitionSetupViewMeta;
   import net.wg.infrastructure.base.meta.impl.AmmunitionSetupViewMeta;
   import net.wg.infrastructure.interfaces.IDAAPIModule;
   import net.wg.utils.StageSizeBoundaries;
   import scaleform.clik.motion.Tween;
   
   public class AmmunitionSetupView extends AmmunitionSetupViewMeta implements IAmmunitionSetupViewMeta
   {
      
      private static const PARAMS_MARGIN_BOTTOM:int = 178;
      
      private static const BOTTOM_PANEL_HEIGHT:int = 35;
      
      private static const PARAMS_ANIM_OFFSET_Y:int = 70;
      
      private static const ANIM_DURATION:int = 300;
      
      private static const GF_H_MARGIN:int = 10;
      
      private static const PARAMS_RIGHT_EMPTY_AREA:int = 19;
      
      private static const PARAMS_Y_LARGE:int = 152;
      
      private static const PARAMS_Y_MEDIUM:int = 143;
      
      private static const PARAMS_Y_SMALL:int = 125;
      
      private static const PARAMS_Y_TINY:int = 165;
       
      
      public var gfContent:AmmunitionSetupViewInject = null;
      
      public var params:VehicleParametersWithHighlight = null;
      
      private var _paramsTween:Tween;
      
      private var _paramsPositionInited:Boolean = false;
      
      private var _appStage:Stage;
      
      public function AmmunitionSetupView()
      {
         this._appStage = App.stage;
         super();
         mouseChildren = false;
         mouseEnabled = false;
      }
      
      override public function updateStage(param1:Number, param2:Number) : void
      {
         _originalWidth = param1;
         _originalHeight = param2;
         if(this.gfContent)
         {
            this.gfContent.setSize(param1 + GF_H_MARGIN * 2,param2 + BOTTOM_PANEL_HEIGHT);
         }
         this.updateParamsVertLayout();
      }
      
      override protected function initialize() : void
      {
         super.initialize();
         this.params.alpha = 0;
      }
      
      override protected function onPopulate() : void
      {
         super.onPopulate();
         if(this.gfContent != null)
         {
            registerFlashComponentS(IDAAPIModule(this.gfContent),HANGAR_ALIASES.AMMUNITION_SETUP_VIEW_INJECT);
            this.gfContent.x = -GF_H_MARGIN;
            this.gfContent.y = 0;
         }
         this.params.showShadowLipWhenOverflow = true;
         this.params.snapHeightToRenderers = false;
         this.params.hideBg();
         this.params.forceInvalidateOnDataChange = true;
         this.updateParamsVertLayout();
         registerFlashComponentS(this.params,HANGAR_ALIASES.AMMUNITION_SETUP_VIEW_VEHICLE_PARAMS);
         setFocus(this.gfContent);
         if(App.gameInputMgr)
         {
            App.gameInputMgr.setKeyHandler(Keyboard.ESCAPE,KeyboardEvent.KEY_DOWN,this.onEscapeKeyDown,true);
         }
      }
      
      override protected function onDispose() : void
      {
         this.clearTween();
         if(App.gameInputMgr)
         {
            App.gameInputMgr.clearKeyHandler(Keyboard.ESCAPE,KeyboardEvent.KEY_DOWN,this.onEscapeKeyDown);
         }
         this.gfContent = null;
         this.params = null;
         this._appStage = null;
         super.onDispose();
      }
      
      public function as_gfSizeUpdated(param1:int, param2:int) : void
      {
         this.params.x = param1 + param2 + PARAMS_RIGHT_EMPTY_AREA - this.params.width >> 0;
         if(!this._paramsPositionInited)
         {
            this._paramsPositionInited = true;
            this.showView();
         }
      }
      
      public function as_onAnimationEnd() : void
      {
         mouseChildren = true;
         mouseEnabled = true;
      }
      
      public function as_showCloseAnim() : void
      {
         this.clearTween();
         this._appStage.dispatchEvent(new Event(HangarAmunitionSwitchAnimator.MAKE_HANGAR_VISIBILE));
         this.onHideAnimComplete();
      }
      
      private function clearTween() : void
      {
         if(this._paramsTween)
         {
            this._paramsTween.dispose();
            this._paramsTween = null;
         }
      }
      
      private function updateParamsVertLayout() : void
      {
         var _loc1_:int = PARAMS_Y_LARGE;
         if(_originalWidth < StageSizeBoundaries.WIDTH_1366)
         {
            _loc1_ = PARAMS_Y_TINY;
         }
         else if(_originalWidth < StageSizeBoundaries.WIDTH_1600 && _originalHeight < StageSizeBoundaries.HEIGHT_900)
         {
            _loc1_ = PARAMS_Y_SMALL;
         }
         else if(_originalHeight < StageSizeBoundaries.HEIGHT_1080)
         {
            _loc1_ = PARAMS_Y_MEDIUM;
         }
         this.params.y = _loc1_;
         this.params.height = _originalHeight - this.params.y - PARAMS_MARGIN_BOTTOM ^ 0;
         invalidateSize();
      }
      
      private function showView() : void
      {
         this.clearTween();
         this._paramsTween = new Tween(ANIM_DURATION,this.params,{
            "alpha":1,
            "y":this.params.y
         },{
            "fastTransform":false,
            "ease":Regular.easeOut,
            "onComplete":this.onShowComplete
         });
         this.params.y += PARAMS_ANIM_OFFSET_Y;
         this._appStage.dispatchEvent(new Event(HangarAmunitionSwitchAnimator.AMMUNITION_VIEW_SHOW_ANIM_START));
      }
      
      private function onHideAnimComplete() : void
      {
         this.clearTween();
         this._appStage.dispatchEvent(new Event(HangarAmunitionSwitchAnimator.PLAY_ANIM_SHOW_HANGAR));
         onCloseS();
      }
      
      private function onShowComplete() : void
      {
         this.clearTween();
         this._appStage.dispatchEvent(new Event(HangarAmunitionSwitchAnimator.AMMUNITION_VIEW_SHOW_ANIM_COMPLETE));
      }
      
      private function onEscapeKeyDown() : void
      {
         onEscapePressS();
      }
   }
}
