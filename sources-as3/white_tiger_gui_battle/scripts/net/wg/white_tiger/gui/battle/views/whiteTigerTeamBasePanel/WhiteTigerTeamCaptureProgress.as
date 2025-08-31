package net.wg.white_tiger.gui.battle.views.whiteTigerTeamBasePanel
{
   import flash.display.BitmapData;
   import flash.display.Graphics;
   import flash.display.Sprite;
   import flash.geom.Rectangle;
   import net.wg.data.constants.Values;
   import net.wg.gui.battle.random.views.teamBasesPanel.TeamCaptureProgress;
   
   public class WhiteTigerTeamCaptureProgress extends TeamCaptureProgress
   {
      
      private static const SCALE_9_GRID:Rectangle = new Rectangle(10,1,1,35);
      
      private static const WIDTH:int = 360;
      
      private static const OFFSET_X:int = -8;
      
      private static const OFFSET_Y:int = -8;
      
      private static const OFFSET_WIDTH:int = 16;
       
      
      private var _scaleSprite:Sprite;
      
      public function WhiteTigerTeamCaptureProgress()
      {
         this._scaleSprite = new Sprite();
         super();
         this._scaleSprite.x = OFFSET_X;
         this._scaleSprite.y = OFFSET_Y;
         barColor.addChild(this._scaleSprite);
      }
      
      override protected function getFillTarget() : Sprite
      {
         return this._scaleSprite;
      }
      
      override protected function drawGraphic() : void
      {
         if(_bitmapSrcPrefix == Values.EMPTY_STR || _colorType == Values.EMPTY_STR)
         {
            return;
         }
         var _loc1_:String = _bitmapSrcPrefix + _colorType;
         var _loc2_:BitmapData = App.utils.classFactory.getObject(_loc1_) as BitmapData;
         if(!_loc2_)
         {
            return;
         }
         this.drawBitmap(_fillTarget,_loc2_);
         this.x = -WIDTH >> 1;
      }
      
      override public function set scaleX(param1:Number) : void
      {
         this._scaleSprite.width = param1 * WIDTH + OFFSET_WIDTH;
      }
      
      override public function get scaleX() : Number
      {
         return (this._scaleSprite.width - OFFSET_WIDTH) / WIDTH;
      }
      
      override public function set colorType(param1:String) : void
      {
         super.colorType = param1;
      }
      
      private function drawBitmap(param1:Sprite, param2:BitmapData) : void
      {
         var _loc3_:Rectangle = null;
         var _loc4_:Vector.<Number> = null;
         var _loc5_:Vector.<Number> = null;
         var _loc10_:int = 0;
         var _loc11_:int = 0;
         var _loc12_:int = 0;
         _loc3_ = SCALE_9_GRID;
         _loc4_ = Vector.<Number>([0,_loc3_.left,_loc3_.right,param2.width]);
         _loc5_ = Vector.<Number>([0,_loc3_.top,_loc3_.bottom,param2.height]);
         var _loc6_:Graphics = param1.graphics;
         var _loc7_:int = _loc4_.length;
         var _loc8_:int = _loc5_.length;
         var _loc9_:int = 1;
         while(_loc9_ < _loc7_)
         {
            _loc10_ = 1;
            while(_loc10_ < _loc8_)
            {
               _loc11_ = _loc4_[_loc9_ - 1];
               _loc12_ = _loc5_[_loc10_ - 1];
               _loc6_.beginBitmapFill(param2);
               _loc6_.drawRect(_loc11_,_loc12_,_loc4_[_loc9_] - _loc11_,_loc5_[_loc10_] - _loc12_);
               _loc6_.endFill();
               _loc10_++;
            }
            _loc9_++;
         }
         param1.scale9Grid = _loc3_;
      }
      
      override public function onDispose() : void
      {
         this._scaleSprite = null;
         super.onDispose();
      }
   }
}
