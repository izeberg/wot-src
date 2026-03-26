package net.wg.gui.battle.views.widgetsPanel.propellantGun
{
   import flash.display.MovieClip;
   import flash.text.TextField;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   
   public class PropellantGunDamageIndicator extends MovieClip implements IDisposable
   {
      
      private static const DAMAGE_VALUE_SNAP_FACTOR:uint = 5;
       
      
      public var damageTF:TextField;
      
      private var _isDisposed:Boolean = false;
      
      private var _damageValue:int = -1;
      
      public function PropellantGunDamageIndicator()
      {
         super();
      }
      
      protected function onDispose() : void
      {
         this.damageTF = null;
      }
      
      public final function dispose() : void
      {
         if(this._isDisposed)
         {
            return;
         }
         this.onDispose();
         this._isDisposed = true;
      }
      
      public function isDisposed() : Boolean
      {
         return this._isDisposed;
      }
      
      public function set state(param1:String) : void
      {
         if(param1 == this.currentFrameLabel)
         {
            return;
         }
         this.gotoAndStop(param1);
         this.damageTF.text = this._damageValue.toString();
      }
      
      public function set damage(param1:Number) : void
      {
         param1 = (param1 / DAMAGE_VALUE_SNAP_FACTOR | 0) * DAMAGE_VALUE_SNAP_FACTOR;
         if(param1 == this._damageValue)
         {
            return;
         }
         this._damageValue = param1;
         this.damageTF.text = param1.toString();
      }
   }
}
