package net.wg.gui.components.crosshairPanel.components.wt
{
   import flash.display.MovieClip;
   import flash.text.TextField;
   import net.wg.gui.components.crosshairPanel.components.wt.components.PlasmaExtraDamageBraces;
   import net.wg.infrastructure.base.SimpleDisposable;
   
   public class PlasmaExtraDamage extends SimpleDisposable
   {
      
      private static const GLOW_LBL:String = "glow";
      
      private static const ICON_X_OFFSET:int = -6;
      
      private static const ICON_GAP:int = -8;
      
      private static const BRACES_X_OFFSET:int = -12;
       
      
      public var textField:TextField = null;
      
      public var textFieldRed:TextField = null;
      
      public var icon:MovieClip = null;
      
      public var braces:PlasmaExtraDamageBraces = null;
      
      private var _plasmaSaved:Number = 0;
      
      private var _text:String = "";
      
      private var _oldContentWidth:int = 0;
      
      private var _totalFrames:int = 0;
      
      public function PlasmaExtraDamage()
      {
         super();
         this.textFieldRed.visible = false;
         this._totalFrames = totalFrames;
         addFrameScript(this._totalFrames - 2,this.glowEnd);
      }
      
      override protected function onDispose() : void
      {
         addFrameScript(this._totalFrames - 2,null);
         this.textField = null;
         this.textFieldRed = null;
         this.icon = null;
         this.braces.dispose();
         this.braces = null;
      }
      
      public function layout() : void
      {
         var _loc1_:int = this.icon.width + this.textField.textWidth + ICON_GAP;
         if(this._oldContentWidth == _loc1_)
         {
            return;
         }
         this._oldContentWidth = _loc1_;
         this.icon.x = -(_loc1_ >> 1) + ICON_X_OFFSET;
         this.textField.x = this.textFieldRed.x = this.icon.x + this.icon.width + ICON_GAP;
         this.braces.x = this.icon.x + BRACES_X_OFFSET;
         this.braces.layout(_loc1_);
      }
      
      public function setPlasmaSaved(param1:Number) : void
      {
         this._plasmaSaved = param1;
      }
      
      public function showPlasma(param1:Number, param2:Number, param3:String) : void
      {
         if(param1 <= 0)
         {
            return;
         }
         this.label = param3;
         if(param1 == param2)
         {
            if(param1 <= this._plasmaSaved)
            {
               this.braces.showBraces(false);
            }
            else
            {
               this.braces.hideBraces(false);
            }
            return;
         }
         if(param1 <= this._plasmaSaved)
         {
            this.braces.showBraces();
         }
         else
         {
            this.braces.hideBraces();
         }
         if(param1 < param2)
         {
            this.showGlow();
         }
      }
      
      private function showGlow() : void
      {
         this.textField.visible = false;
         this.textFieldRed.visible = true;
         gotoAndPlay(GLOW_LBL);
      }
      
      private function glowEnd() : void
      {
         this.textField.visible = true;
         this.textFieldRed.visible = false;
      }
      
      private function set label(param1:String) : void
      {
         if(this._text == param1)
         {
            return;
         }
         this._text = param1;
         this.textField.text = param1;
         this.textFieldRed.text = param1;
         this.layout();
      }
   }
}
