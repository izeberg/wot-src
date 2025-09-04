package net.wg.gui.battle.views.vehicleMarkers
{
   import flash.display.MovieClip;
   import flash.text.TextFieldAutoSize;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   
   public class DamageLabelAnimatedScreen extends MovieClip implements IDisposable
   {
       
      
      public var damageLabel:DamageLabel;
      
      private var _baseDisposed:Boolean = false;
      
      public function DamageLabelAnimatedScreen()
      {
         super();
         this.damageLabel.autoSize = TextFieldAutoSize.CENTER;
      }
      
      protected function onDispose() : void
      {
         this.damageLabel.dispose();
         this.damageLabel = null;
      }
      
      public final function dispose() : void
      {
         if(this._baseDisposed)
         {
            return;
         }
         this.onDispose();
         this._baseDisposed = true;
      }
      
      public function isDisposed() : Boolean
      {
         return this._baseDisposed;
      }
      
      public function setLabel(param1:String, param2:String) : void
      {
         this.damageLabel.color = param2;
         this.damageLabel.text = param1;
      }
   }
}
