package net.wg.gui.battle.views.minimap.components.entries.personal
{
   import flash.display.Graphics;
   import flash.display.Shape;
   import flash.display.Sprite;
   import net.wg.gui.utils.GraphicsUtilities;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   
   public class ViewRangeSectorMinimapEntry extends Sprite implements IDisposable
   {
      
      private static const AREA_MAX_SIZE_REAL:int = 210;
      
      private static const SECTOR_BORDER_COLOR:uint = 5301276;
      
      private static const SECTOR_FILL_COLOR:uint = 1744896;
      
      private static const SECTOR_FILL_ALPHA:Number = 0.2;
       
      
      private var _dynamicMC:Shape = null;
      
      private var _circleDiameterCoeff:Number = 0;
      
      private var _currentSectorRadius:Number = 0;
      
      private var _disposed:Boolean = false;
      
      public function ViewRangeSectorMinimapEntry()
      {
         super();
      }
      
      public function as_addSector(param1:Number, param2:Number) : void
      {
         if(this._dynamicMC == null)
         {
            this._dynamicMC = this.initializeSector(param1,param2);
         }
      }
      
      public function as_delSector() : void
      {
         if(this._dynamicMC)
         {
            removeChild(this._dynamicMC);
            this._dynamicMC = null;
         }
      }
      
      public function as_initArenaSize(param1:int) : void
      {
         var _loc2_:Number = AREA_MAX_SIZE_REAL / param1;
         this._circleDiameterCoeff = _loc2_ * 2;
      }
      
      public function as_updateSectorRadius(param1:Number) : void
      {
         var _loc2_:Number = NaN;
         if(this._dynamicMC && this._currentSectorRadius != param1)
         {
            this._currentSectorRadius = param1;
            _loc2_ = this._currentSectorRadius * this._circleDiameterCoeff * 2;
            this._dynamicMC.width = _loc2_;
            this._dynamicMC.height = _loc2_;
         }
      }
      
      public final function dispose() : void
      {
         this._disposed = true;
         this.as_delSector();
      }
      
      public function isDisposed() : Boolean
      {
         return this._disposed;
      }
      
      private function initializeSector(param1:Number, param2:Number) : Shape
      {
         var _loc3_:Shape = new Shape();
         addChild(_loc3_);
         var _loc4_:Graphics = _loc3_.graphics;
         _loc4_.clear();
         _loc4_.lineStyle(1,SECTOR_BORDER_COLOR);
         _loc4_.beginFill(SECTOR_FILL_COLOR,SECTOR_FILL_ALPHA);
         GraphicsUtilities.drawSector(_loc4_,AREA_MAX_SIZE_REAL,param2);
         _loc4_.endFill();
         _loc4_.lineStyle(0,16777215,0.01);
         _loc4_.drawCircle(0,0,AREA_MAX_SIZE_REAL);
         var _loc5_:Number = param1 * this._circleDiameterCoeff;
         _loc3_.width = _loc5_;
         _loc3_.height = _loc5_;
         return _loc3_;
      }
   }
}
