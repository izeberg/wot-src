package net.wg.gui.battle.views.widgetsPanel.autoreloaderSurge
{
   import flash.display.MovieClip;
   import flash.geom.Matrix;
   import flash.geom.Rectangle;
   import net.wg.data.constants.Linkages;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   import net.wg.utils.IClassFactory;
   
   public class AutoreloaderSurgeSectors extends MovieClip implements IDisposable
   {
      
      private static const MIN_SECTORS:int = 2;
      
      private static const MAX_SECTORS:int = 4;
      
      private static const DEG_TO_RAD:Number = Math.PI / 180;
      
      private static const ROTATION_STEPS:Vector.<Number> = new <Number>[0,0,26,17.333,13];
      
      private static const SECTOR_LINKAGES:Vector.<String> = new <String>["","",Linkages.AUTORELOADER_SURGE_SECTOR_2,Linkages.AUTORELOADER_SURGE_SECTOR_3,Linkages.AUTORELOADER_SURGE_SECTOR_4];
       
      
      private var _sectors:Vector.<AutoreloaderSurgeSector> = null;
      
      private var _disposed:Boolean = false;
      
      public function AutoreloaderSurgeSectors()
      {
         super();
         this._sectors = new Vector.<AutoreloaderSurgeSector>(0);
      }
      
      private static function rotateAroundCenter(param1:MovieClip, param2:Number) : void
      {
         var _loc3_:Rectangle = param1.getBounds(param1);
         var _loc4_:Number = _loc3_.x + _loc3_.width * 0.5;
         var _loc5_:Number = _loc3_.y + _loc3_.height * 0.5;
         var _loc6_:Number = param2 * DEG_TO_RAD;
         var _loc7_:Number = Math.cos(_loc6_);
         var _loc8_:Number = Math.sin(_loc6_);
         var _loc9_:Matrix = param1.transform.matrix;
         _loc9_.translate(-_loc4_,-_loc5_);
         _loc9_.concat(new Matrix(_loc7_,_loc8_,-_loc8_,_loc7_));
         _loc9_.translate(_loc4_,_loc5_);
         param1.transform.matrix = _loc9_;
      }
      
      public function setup(param1:int) : void
      {
         var _loc7_:AutoreloaderSurgeSector = null;
         this.removeAll();
         if(param1 < MIN_SECTORS || param1 > MAX_SECTORS)
         {
            DebugUtils.LOG_ERROR("AutoreloaderSurgeSectors: invalid sector count " + param1);
            return;
         }
         var _loc2_:IClassFactory = App.utils.classFactory;
         var _loc3_:Number = ROTATION_STEPS[param1];
         var _loc4_:String = SECTOR_LINKAGES[param1];
         var _loc5_:Number = _loc3_ * (param1 - 1);
         var _loc6_:int = 0;
         while(_loc6_ < param1)
         {
            _loc7_ = _loc2_.getComponent(_loc4_,AutoreloaderSurgeSector);
            rotateAroundCenter(_loc7_,_loc6_ * _loc3_ - _loc5_);
            addChild(_loc7_);
            this._sectors.push(_loc7_);
            _loc6_++;
         }
      }
      
      public function setProgress(param1:Array) : void
      {
         var _loc5_:Number = NaN;
         var _loc2_:int = this._sectors.length;
         var _loc3_:int = param1.length;
         var _loc4_:int = 0;
         while(_loc4_ < _loc2_)
         {
            _loc5_ = _loc4_ < _loc3_ ? Number(param1[_loc4_]) : Number(0);
            this._sectors[_loc4_].setProgress(_loc5_);
            _loc4_++;
         }
      }
      
      public function playActivation(param1:int) : void
      {
         var _loc2_:int = this._sectors.length;
         var _loc3_:int = 0;
         while(_loc3_ < _loc2_)
         {
            if(_loc3_ == param1)
            {
               this._sectors[_loc3_].playActivation();
            }
            else if(_loc3_ < param1)
            {
               this._sectors[_loc3_].playCooldown();
            }
            _loc3_++;
         }
      }
      
      public function setChargingSector(param1:int) : void
      {
         var _loc2_:int = this._sectors.length;
         var _loc3_:int = 0;
         while(_loc3_ < _loc2_)
         {
            this._sectors[_loc3_].setCharging(_loc3_ == param1);
            _loc3_++;
         }
      }
      
      public function playRecharge(param1:int) : void
      {
         var _loc2_:int = this._sectors.length;
         var _loc3_:int = 0;
         while(_loc3_ < param1 && _loc3_ < _loc2_)
         {
            this._sectors[_loc3_].playRecharge();
            _loc3_++;
         }
      }
      
      public function dispose() : void
      {
         this.removeAll();
         this._sectors = null;
         this._disposed = true;
      }
      
      public function isDisposed() : Boolean
      {
         return this._disposed;
      }
      
      private function removeAll() : void
      {
         var _loc1_:AutoreloaderSurgeSector = null;
         while(this._sectors.length > 0)
         {
            _loc1_ = this._sectors.pop();
            _loc1_.dispose();
            removeChild(_loc1_);
         }
      }
   }
}
