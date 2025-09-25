package net.wg.gui.battle.views.vehicleMarkers
{
   import flash.display.DisplayObject;
   import flash.display.DisplayObjectContainer;
   import flash.display.MovieClip;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   
   public class VehicleMarkerFxContainer extends MovieClip implements IDisposable
   {
      
      private static const IDLE_FRAME_LABEL:String = "idle";
      
      private static const RAMMING_FRAME_LABEL:String = "ramming";
       
      
      public var content:DisplayObjectContainer;
      
      private var _baseDisposed:Boolean = false;
      
      public function VehicleMarkerFxContainer()
      {
         super();
      }
      
      protected function onDispose() : void
      {
         while(this.content.numChildren > 0)
         {
            this.content.removeChild(this.content.getChildAt(0));
         }
         this.content = null;
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
      
      public function showRammingEffect(param1:DisplayObjectContainer) : void
      {
         if(this.currentFrameLabel != IDLE_FRAME_LABEL)
         {
            return;
         }
         this.setupTargetContent(param1);
         this.gotoAndPlay(RAMMING_FRAME_LABEL);
      }
      
      private function setupTargetContent(param1:DisplayObjectContainer) : void
      {
         if(!param1)
         {
            return;
         }
         var _loc2_:int = param1.numChildren;
         var _loc3_:DisplayObject = null;
         var _loc4_:int = 0;
         var _loc5_:int = 0;
         while(_loc5_ < _loc2_)
         {
            _loc3_ = param1.getChildAt(_loc4_);
            if(_loc3_ == this)
            {
               _loc4_++;
            }
            else
            {
               this.content.addChild(_loc3_);
            }
            _loc5_++;
         }
      }
   }
}
