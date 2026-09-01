package net.wg.white_tiger.gui.battle.views.whiteTigerTeamBasePanel
{
   import flash.display.MovieClip;
   import net.wg.gui.battle.random.views.teamBasesPanel.TeamCaptureBar;
   import net.wg.infrastructure.events.ColorSchemeEvent;
   import net.wg.infrastructure.managers.IColorSchemeManager;
   import org.idmedia.as3commons.util.StringUtils;
   
   public class WhiteTigerTeamCaptureBar extends TeamCaptureBar
   {
      
      private static const GENERATOR_STATE_NORMAL:String = "normal";
      
      private static const GENERATOR_STATE_LOCKED:String = "locked";
      
      private static const GENERATOR_STATE_LOCKED_COLOR_BLIND:String = "_colorBlind";
      
      private static const TIME_LEFT_LOCKED_TEXT:String = "--:--";
      
      private static const TWEEN_EASE_NONE:Array = [0.032,0.068,0.116,0.152,0.2,0.232,0.268,0.316,0.352,0.4,0.432,0.468,0.516,0.552,0.6,0.664,0.668,0.716,0.752,0.8,0.832,0.868,0.916,0.952,1];
       
      
      public var generatorIcon:MovieClip = null;
      
      public var timerIcon:MovieClip = null;
      
      public var tankIcon:MovieClip = null;
      
      private var _colorMgr:IColorSchemeManager;
      
      private var _isColorBlind:Boolean = false;
      
      public function WhiteTigerTeamCaptureBar()
      {
         this._colorMgr = App.colorSchemeMgr;
         super();
         this._isColorBlind = this._colorMgr.getIsColorBlindS();
         this._colorMgr.addEventListener(ColorSchemeEvent.SCHEMAS_UPDATED,this.onColorSchemasUpdatedHandler);
      }
      
      override public function dispose() : void
      {
         this.generatorIcon = null;
         this.timerIcon = null;
         this.tankIcon = null;
         this._colorMgr.removeEventListener(ColorSchemeEvent.SCHEMAS_UPDATED,this.onColorSchemasUpdatedHandler);
         this._colorMgr = null;
         super.dispose();
      }
      
      override protected function getEaseArray(param1:Number) : Array
      {
         return TWEEN_EASE_NONE;
      }
      
      override public function setCaptured(param1:String) : void
      {
         this.updateTitleIcon(param1);
         super.setCaptured(param1);
      }
      
      override public function setData(param1:Number, param2:Number, param3:String, param4:String, param5:Number, param6:String, param7:String) : void
      {
         this.updateTitleIcon(param4);
         super.setData(param1,param2,param3,param4,param5,param6,param7);
      }
      
      override public function updateCaptureData(param1:Number, param2:Boolean, param3:Boolean, param4:Number, param5:String, param6:String, param7:String, param8:String, param9:Boolean = true) : void
      {
         this.updateTitleIcon(param7);
         super.updateCaptureData(param1,param2,param3,param4,param5,param6,param7,param8,param9);
      }
      
      private function updateTitleIcon(param1:String) : void
      {
         this.generatorIcon.x = textField.x + (textField.width - textField.textWidth >> 1);
         this.tankIcon.visible = this.timerIcon.visible = this.generatorIcon.visible = StringUtils.isNotEmpty(param1);
      }
      
      public function lockGenerator(param1:Boolean) : void
      {
         this.generatorIcon.gotoAndStop(!!param1 ? this.getGeneratorIconState() : GENERATOR_STATE_NORMAL);
         if(param1)
         {
            tfTimeLeft.text = TIME_LEFT_LOCKED_TEXT;
         }
      }
      
      private function onColorSchemasUpdatedHandler(param1:ColorSchemeEvent) : void
      {
         this._isColorBlind = this._colorMgr.getIsColorBlindS();
         if(this.generatorIcon.currentLabel == GENERATOR_STATE_NORMAL)
         {
            return;
         }
         this.generatorIcon.gotoAndStop(this.getGeneratorIconState());
      }
      
      private function getGeneratorIconState() : String
      {
         return !!this._isColorBlind ? GENERATOR_STATE_LOCKED_COLOR_BLIND : GENERATOR_STATE_LOCKED;
      }
   }
}
