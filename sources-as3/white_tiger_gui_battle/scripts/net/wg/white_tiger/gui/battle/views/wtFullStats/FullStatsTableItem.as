package net.wg.white_tiger.gui.battle.views.wtFullStats
{
   import flash.geom.ColorTransform;
   import net.wg.gui.battle.random.views.stats.components.fullStats.tableItem.StatsTableItem;
   import net.wg.gui.battle.views.stats.constants.FullStatsValidationType;
   import net.wg.white_tiger.gui.battle.views.shared.HunterResurrectTimer;
   
   public class FullStatsTableItem extends StatsTableItem
   {
      
      private static const VEHICLE_ICON_RESURRECT_COLOR_TRANSFORM:ColorTransform = new ColorTransform(0.5,0.5,0.5,1,179,0,0,0);
      
      private static const NUM_ROWS:int = 6;
       
      
      private var _resurrectTimer:HunterResurrectTimer = null;
      
      private var _isResurrect:Boolean = false;
      
      public function FullStatsTableItem(param1:FullStatsTable, param2:int, param3:int)
      {
         super(param1,param2,param3);
         var _loc4_:int = param2 * this.numRows + param3;
         this._resurrectTimer = param1.resurrectTimerCollection[_loc4_];
         this._resurrectTimer.visible = false;
         this._resurrectTimer.finishCallback = this.onRespawnTimerFinished;
      }
      
      override public function reset() : void
      {
         this._isResurrect = false;
         super.reset();
      }
      
      override public function setIsDead(param1:Boolean) : void
      {
         super.setIsDead(param1 && !this._isResurrect);
      }
      
      override public function setIsSquadPersonal(param1:Boolean) : void
      {
      }
      
      override protected function onDispose() : void
      {
         this._resurrectTimer = null;
         super.onDispose();
      }
      
      override protected function draw() : void
      {
         super.draw();
         if(isInvalid(FullStatsValidationType.COLORS))
         {
            if(this._isResurrect)
            {
               vehicleIcon.transform.colorTransform = VEHICLE_ICON_RESURRECT_COLOR_TRANSFORM;
            }
         }
      }
      
      override protected function applyTextColor(param1:uint) : void
      {
         super.applyTextColor(param1);
         var _loc2_:ColorTransform = new ColorTransform();
         _loc2_.color = param1;
         vehicleTypeIcon.transform.colorTransform = _loc2_;
      }
      
      public function setResurrectTimer(param1:Number, param2:Number, param3:Number) : void
      {
         this._resurrectTimer.updateTime(param1,param2,param3);
      }
      
      private function onRespawnTimerFinished() : void
      {
         this.isResurrect = false;
      }
      
      override protected function get numRows() : uint
      {
         return NUM_ROWS;
      }
      
      public function set isResurrect(param1:Boolean) : void
      {
         if(param1 == this._isResurrect)
         {
            return;
         }
         this._isResurrect = this._resurrectTimer.visible = param1;
         invalidate(FullStatsValidationType.COLORS);
         if(this._isResurrect)
         {
            super.setIsDead(false);
         }
      }
   }
}
