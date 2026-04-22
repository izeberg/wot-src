package net.wg.gui.battle.views.decorativeCrosshair
{
   import flash.display.BlendMode;
   import flash.display.MovieClip;
   import net.wg.data.constants.generated.CROSSHAIR_VIEW_ID;
   import net.wg.data.constants.generated.DECORATIVE_CROSSHAIR_CONSTS;
   import net.wg.infrastructure.base.meta.ITemperatureGunOverheatDecorativeCrosshairMeta;
   import net.wg.infrastructure.base.meta.impl.TemperatureGunOverheatDecorativeCrosshairMeta;
   import net.wg.infrastructure.events.ColorSchemeEvent;
   
   public class TemperatureGunOverheatDecorativeCrosshair extends TemperatureGunOverheatDecorativeCrosshairMeta implements ITemperatureGunOverheatDecorativeCrosshairMeta
   {
      
      private static const SCALE_ARCADE:Number = 0.86;
      
      private static const SCALE_SNIPER:Number = 1;
      
      private static const STATE_OVERHEAT:String = "overheat";
      
      private static const STATE_WARNING:String = "warning";
      
      private static const STATE_EMPTY:String = "empty";
      
      private static const OFF_PREFIX:String = "_off";
      
      private static const COLOR_BLIND_FRAME:int = 2;
      
      private static const NORMAL_COLOR_FRAME:int = 1;
      
      private static const STATES_MAP:Object = {};
      
      {
         STATES_MAP[DECORATIVE_CROSSHAIR_CONSTS.HIDE_STATE] = STATE_EMPTY;
         STATES_MAP[DECORATIVE_CROSSHAIR_CONSTS.WARNING_STATE] = STATE_WARNING;
         STATES_MAP[DECORATIVE_CROSSHAIR_CONSTS.SHOW_STATE] = STATE_OVERHEAT;
      }
      
      public var heatProgress:MovieClip = null;
      
      private var _crosshairType:int = 1;
      
      private var _isColorBlind:Boolean = false;
      
      private var _prevState:String = "empty";
      
      public function TemperatureGunOverheatDecorativeCrosshair()
      {
         super();
         _state = STATE_EMPTY;
      }
      
      override public function as_setState(param1:String, param2:Boolean) : void
      {
         var _loc3_:String = STATES_MAP[param1];
         if(!_loc3_ || _state == _loc3_ && !param2)
         {
            return;
         }
         this._prevState = _state;
         _state = _loc3_;
         this.updateState(param2);
      }
      
      override public function updateScale(param1:int) : void
      {
         this.heatProgress.scaleX = this.heatProgress.scaleY = param1 == CROSSHAIR_VIEW_ID.ARCADE ? Number(SCALE_ARCADE) : Number(SCALE_SNIPER);
         this._crosshairType = param1;
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this.blendMode = BlendMode.SCREEN;
         App.colorSchemeMgr.addEventListener(ColorSchemeEvent.SCHEMAS_UPDATED,this.onColorSchemeMgrSchemasUpdatedHandler);
         this.updateColorBlindMode();
         this.updateState(true);
      }
      
      override protected function onDispose() : void
      {
         this.heatProgress = null;
         App.colorSchemeMgr.removeEventListener(ColorSchemeEvent.SCHEMAS_UPDATED,this.onColorSchemeMgrSchemasUpdatedHandler);
         super.onDispose();
      }
      
      private function updateState(param1:Boolean = false) : void
      {
         var _loc2_:String = !!param1 ? INSTANTLY_POSTFIX : "";
         switch(_state)
         {
            case STATE_OVERHEAT:
               this.heatProgress.gotoAndPlay(STATE_OVERHEAT + _loc2_);
               break;
            case STATE_EMPTY:
               if(param1 || this._prevState == STATE_EMPTY)
               {
                  this.heatProgress.gotoAndStop(STATE_EMPTY);
               }
               else
               {
                  this.heatProgress.gotoAndPlay(this._prevState + OFF_PREFIX);
               }
               break;
            case STATE_WARNING:
               this.heatProgress.gotoAndPlay(STATE_WARNING + _loc2_);
         }
      }
      
      private function updateColorBlindMode() : void
      {
         var _loc1_:Boolean = App.colorSchemeMgr.getIsColorBlindS();
         if(this._isColorBlind != _loc1_)
         {
            this._isColorBlind = _loc1_;
            gotoAndStop(!!this._isColorBlind ? COLOR_BLIND_FRAME : NORMAL_COLOR_FRAME);
            this.updateState(true);
            this.updateScale(this._crosshairType);
         }
      }
      
      private function onColorSchemeMgrSchemasUpdatedHandler(param1:ColorSchemeEvent) : void
      {
         this.updateColorBlindMode();
      }
   }
}
