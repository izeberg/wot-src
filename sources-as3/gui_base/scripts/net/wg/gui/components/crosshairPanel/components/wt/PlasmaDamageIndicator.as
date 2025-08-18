package net.wg.gui.components.crosshairPanel.components.wt
{
   import flash.display.MovieClip;
   import flash.text.TextField;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   
   public class PlasmaDamageIndicator extends MovieClip implements IDisposable
   {
      
      private static const SHOW_GLOW_FRAME_LABEL:String = "start";
       
      
      public var textField:TextField = null;
      
      public var glow:MovieClip = null;
      
      private var _text:String = "";
      
      public function PlasmaDamageIndicator()
      {
         super();
      }
      
      public final function dispose() : void
      {
         this.textField = null;
         this.glow = null;
      }
      
      public function isDisposed() : Boolean
      {
         return false;
      }
      
      public function showGlow() : void
      {
         this.glow.gotoAndPlay(SHOW_GLOW_FRAME_LABEL);
      }
      
      public function set label(param1:String) : void
      {
         if(this._text == param1)
         {
            return;
         }
         this._text = param1;
         this.textField.text = param1;
      }
   }
}
