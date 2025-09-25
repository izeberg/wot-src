package net.wg.gui.battle.views.decorativeCrosshair
{
   import net.wg.data.constants.generated.CROSSHAIR_VIEW_ID;
   import net.wg.gui.battle.views.decorativeCrosshair.accuracy.AccuracyProgressbar;
   import net.wg.gui.battle.views.decorativeCrosshair.accuracy.SpeedLimitMark;
   import net.wg.infrastructure.base.meta.IAccuracyStackDecorativeCrosshairMeta;
   import net.wg.infrastructure.base.meta.impl.AccuracyStackDecorativeCrosshairMeta;
   
   public class AccuracyStackDecorativeCrosshair extends AccuracyStackDecorativeCrosshairMeta implements IAccuracyStackDecorativeCrosshairMeta
   {
      
      private static const ARCADE_POSITION:int = 520;
      
      private static const SNIPER_POSITION:int = 675;
      
      private static const SNIPER_SCALE:Number = 1;
      
      private static const ARCADE_SCALE:Number = 0.76;
      
      private static const ARCADE_POSITION_MARK_LEFT:int = -504;
      
      private static const SNIPER_POSITION_MARK_LEFT:int = -654;
       
      
      public var markLeft:SpeedLimitMark = null;
      
      public var leftProgres:AccuracyProgressbar = null;
      
      public var rightProgres:AccuracyProgressbar = null;
      
      private var _isSpeedLimit:Boolean = false;
      
      private var _isMaxStackGained:Boolean = false;
      
      private var _maxStackCount:int = 4;
      
      public function AccuracyStackDecorativeCrosshair()
      {
         super();
      }
      
      public function as_setInitData(param1:int, param2:int) : void
      {
         this._maxStackCount = param1;
         this.leftProgres.setMaxStackCount(this._maxStackCount);
         this.rightProgres.setMaxStackCount(this._maxStackCount);
         this.markLeft.setSpeed(param2);
         this.updateSpeedLimitMark();
      }
      
      override public function updateScale(param1:int) : void
      {
         if(param1 == CROSSHAIR_VIEW_ID.ARCADE)
         {
            this.leftProgres.scaleX = this.leftProgres.scaleY = this.rightProgres.scaleX = this.rightProgres.scaleY = ARCADE_SCALE;
            this.leftProgres.x = -ARCADE_POSITION;
            this.rightProgres.x = ARCADE_POSITION;
            this.markLeft.x = ARCADE_POSITION_MARK_LEFT;
         }
         else if(param1 == CROSSHAIR_VIEW_ID.SNIPER)
         {
            this.leftProgres.scaleX = this.leftProgres.scaleY = this.rightProgres.scaleX = this.rightProgres.scaleY = SNIPER_SCALE;
            this.leftProgres.x = -SNIPER_POSITION;
            this.rightProgres.x = SNIPER_POSITION;
            this.markLeft.x = SNIPER_POSITION_MARK_LEFT;
         }
      }
      
      public function as_setStacksProgres(param1:int, param2:Number) : void
      {
         this._isMaxStackGained = param1 >= this._maxStackCount;
         this.leftProgres.updateStacksAndProgress(param1,param2,this._isMaxStackGained);
         this.rightProgres.updateStacksAndProgress(param1,param2,this._isMaxStackGained);
         this.updateSpeedLimitMark();
      }
      
      public function as_setSpeedLimitActive(param1:Boolean) : void
      {
         this._isSpeedLimit = param1;
         this.updateSpeedLimitMark();
      }
      
      public function as_setGainingActive(param1:Boolean) : void
      {
         this.leftProgres.gainingActive(param1);
         this.rightProgres.gainingActive(param1);
         this.updateSpeedLimitMark();
      }
      
      private function updateSpeedLimitMark() : void
      {
         this.markLeft.show(this._isSpeedLimit && !this._isMaxStackGained);
      }
      
      override protected function onDispose() : void
      {
         this.leftProgres.dispose();
         this.leftProgres = null;
         this.rightProgres.dispose();
         this.rightProgres = null;
         this.markLeft.dispose();
         this.markLeft = null;
         super.onDispose();
      }
   }
}
