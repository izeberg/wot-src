package net.wg.gui.battle.views.widgetsPanel.power
{
   import com.gskinner.motion.GTween;
   import com.gskinner.motion.GTweener;
   import flash.display.Sprite;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   
   public class TurbineAnimation extends Sprite implements IDisposable
   {
      
      private static const DEFAULT_ROTATION_DURATION:Number = 2;
      
      private static const FULL_CIRCLE_ANGLE:uint = 360;
       
      
      public var turbine:Sprite;
      
      private var _tween:GTween = null;
      
      private var _isDisposed:Boolean = false;
      
      public function TurbineAnimation()
      {
         super();
         this._tween = GTweener.to(this.turbine,DEFAULT_ROTATION_DURATION,{"rotation":FULL_CIRCLE_ANGLE},{
            "repeatCount":0,
            "paused":true
         });
      }
      
      protected function onDispose() : void
      {
         GTweener.remove(this._tween);
         this.turbine = null;
         this._tween = null;
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
      
      public final function isDisposed() : Boolean
      {
         return this._isDisposed;
      }
      
      public function set speedFactor(param1:Number) : void
      {
         this._tween.paused = param1 == 0;
         this._tween.timeScale = param1;
      }
   }
}
