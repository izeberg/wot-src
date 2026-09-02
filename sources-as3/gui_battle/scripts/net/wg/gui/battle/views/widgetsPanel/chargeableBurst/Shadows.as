package net.wg.gui.battle.views.widgetsPanel.chargeableBurst
{
   import flash.display.MovieClip;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   
   public class Shadows extends MovieClip implements IDisposable
   {
      
      private static const NORMAL_SHOW:String = "normalShow";
      
      private static const NORMAL_SHOWN:String = "normalShown";
      
      private static const BURST_MODE_SHOW:String = "burstModeShow";
      
      private static const BURST_MODE_SHOWN:String = "burstModeShown";
       
      
      public var bulletsShadow:BulletsShadow = null;
      
      public var penetrationsShadow:PenetrationsShadow = null;
      
      private var _disposed:Boolean = false;
      
      public function Shadows()
      {
         super();
      }
      
      public final function dispose() : void
      {
         this.bulletsShadow.dispose();
         this.bulletsShadow = null;
         this.penetrationsShadow.dispose();
         this.penetrationsShadow = null;
         this._disposed = true;
      }
      
      public function isDisposed() : Boolean
      {
         return this._disposed;
      }
      
      public function setup(param1:Number, param2:Number) : void
      {
         this.penetrationsShadow.setup(param1);
         this.bulletsShadow.setup(param2);
         this.updateMode(false,true);
      }
      
      public function updateMode(param1:Boolean, param2:Boolean) : void
      {
         if(param2)
         {
            gotoAndStop(!!param1 ? BURST_MODE_SHOWN : NORMAL_SHOWN);
         }
         else
         {
            gotoAndPlay(!!param1 ? BURST_MODE_SHOW : NORMAL_SHOW);
         }
      }
   }
}
