package net.wg.gui.components.crosshairPanel
{
   import flash.geom.Rectangle;
   import flash.utils.getDefinitionByName;
   import net.wg.data.constants.Errors;
   import net.wg.data.constants.Linkages;
   import net.wg.gui.components.crosshairPanel.components.hitIndicator.HitIndicator;
   
   public class CrosshairWithCassette extends CrosshairBase
   {
      
      private static const RELOAD_TIME_BLINK_Y_SHIFT:int = -10;
       
      
      private var _hitMarker:HitIndicator = null;
      
      public function CrosshairWithCassette()
      {
         super();
      }
      
      override public function animShotHitMarker(param1:String) : void
      {
         if(!this._hitMarker)
         {
            this.createHitMarker();
         }
         if(this._hitMarker)
         {
            this._hitMarker.show(param1);
         }
      }
      
      override public function setShotHitMarkerVisibility(param1:Boolean) : void
      {
         if(param1 && !this._hitMarker)
         {
            this.createHitMarker();
         }
         if(this._hitMarker)
         {
            this._hitMarker.visible = param1;
         }
      }
      
      override protected function arrangeReloadTimeBlink() : void
      {
         var _loc1_:Rectangle = null;
         if(isAutoloader)
         {
            _loc1_ = autoloaderComponent.getTimerRect();
            if(_loc1_ != null)
            {
               reloadTimeBlink.x = autoloaderComponent.x + _loc1_.x + (_loc1_.width - reloadTimeBlink.width >> 1) | 0;
               reloadTimeBlink.y = autoloaderComponent.y + _loc1_.y + _loc1_.height + RELOAD_TIME_BLINK_Y_SHIFT | 0;
            }
         }
         else
         {
            super.arrangeReloadTimeBlink();
         }
      }
      
      override protected function onDispose() : void
      {
         if(this._hitMarker)
         {
            this._hitMarker.dispose();
            this._hitMarker = null;
         }
         super.onDispose();
      }
      
      private function createHitMarker() : void
      {
         var _loc1_:Class = getDefinitionByName(Linkages.HIT_MARKER) as Class;
         if(_loc1_)
         {
            this._hitMarker = new _loc1_();
            addChild(this._hitMarker);
            return;
         }
         throw new Error(Linkages.HIT_MARKER + Errors.BAD_LINKAGE);
      }
   }
}
