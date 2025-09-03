package net.wg.gui.battle.views.decorativeCrosshair.overheat
{
   import flash.display.MovieClip;
   import flash.text.TextField;
   import flash.text.TextFieldAutoSize;
   import net.wg.gui.battle.views.decorativeCrosshair.shared.TextWrapper;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   
   public class OverheatCounter extends MovieClip implements IDisposable
   {
      
      public static const STATE_ON:String = "on";
      
      public static const STATE_OFF:String = "off";
       
      
      public var text:TextField = null;
      
      public var activeText:TextWrapper = null;
      
      private var _isDisposed:Boolean = false;
      
      private var _baseDamage:uint = 0;
      
      private var _currentGainDamage:uint = 0;
      
      public function OverheatCounter()
      {
         super();
         this.text.autoSize = TextFieldAutoSize.LEFT;
         this.activeText.textField.autoSize = TextFieldAutoSize.LEFT;
      }
      
      public function setCount(param1:Number) : void
      {
         this.setState(param1 - this._baseDamage);
         this.text.text = param1.toString();
         this.activeText.setText(param1.toString());
      }
      
      public function setDamageData(param1:Number) : void
      {
         this._baseDamage = param1;
      }
      
      private function setState(param1:uint) : void
      {
         if(param1 == this._currentGainDamage)
         {
            return;
         }
         if(this._currentGainDamage == 0)
         {
            gotoAndPlay(STATE_ON);
         }
         else if(param1 == 0)
         {
            gotoAndPlay(STATE_OFF);
         }
         this._currentGainDamage = param1;
      }
      
      public function dispose() : void
      {
         this.activeText.dispose();
         this.activeText = null;
         this.text = null;
         this._isDisposed = true;
      }
      
      public function isDisposed() : Boolean
      {
         return this._isDisposed;
      }
   }
}
