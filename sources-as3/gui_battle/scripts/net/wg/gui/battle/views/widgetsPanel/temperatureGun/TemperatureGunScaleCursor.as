package net.wg.gui.battle.views.widgetsPanel.temperatureGun
{
   import flash.display.MovieClip;
   import flash.display.Sprite;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   
   public class TemperatureGunScaleCursor extends Sprite implements IDisposable
   {
       
      
      public var cursorMC:MovieClip;
      
      private var _baseDisposed:Boolean = false;
      
      private var _progress:Number = 0;
      
      public function TemperatureGunScaleCursor()
      {
         super();
         this.cursorMC.visible = false;
      }
      
      protected function onDispose() : void
      {
         this.cursorMC = null;
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
      
      public final function isDisposed() : Boolean
      {
         return this._baseDisposed;
      }
      
      public function set cursorType(param1:int) : void
      {
         param1++;
         if(param1 == this.cursorMC.currentFrame)
         {
            return;
         }
         this.cursorMC.gotoAndStop(param1);
      }
      
      public function set progress(param1:Number) : void
      {
         param1 = param1 < 0 ? Number(0) : (param1 > 1 ? Number(1) : Number(param1));
         if(param1 == this._progress)
         {
            return;
         }
         this._progress = param1;
         this.cursorMC.visible = param1 != 0;
         if(this.cursorMC.visible)
         {
            this.cursorMC.rotation = param1 * TemperatureGunScaleSector.PROGRESS_ROTATION_ANGLE;
         }
      }
   }
}
