package net.wg.infrastructure.layoutPart.algorithms
{
   import flash.display.DisplayObject;
   import flash.geom.Point;
   import flash.geom.Rectangle;
   import net.wg.infrastructure.layoutPart.BaseLayoutPart;
   import net.wg.infrastructure.layoutPart.LayoutBounds;
   import net.wg.infrastructure.layoutPart.LayoutPartNode;
   
   public class LayoutPartAbsolute extends BaseLayoutPart
   {
       
      
      public function LayoutPartAbsolute(param1:uint)
      {
         super(param1);
      }
      
      override public function getAlgorithmTypeName() : String
      {
         return "absolute";
      }
      
      override public function register(param1:DisplayObject) : void
      {
         var _loc2_:Point = Boolean(param1.parent) ? param1.parent.localToGlobal(new Point(param1.x,param1.y)) : new Point(param1.x,param1.y);
         var _loc3_:Object = {
            "x":_loc2_.x,
            "y":_loc2_.y
         };
         doRegister(param1,_loc3_);
      }
      
      override protected function makePayload(param1:LayoutPartNode) : Object
      {
         var _loc2_:DisplayObject = null;
         var _loc4_:Number = NaN;
         var _loc5_:Number = NaN;
         var _loc6_:Number = NaN;
         var _loc7_:Number = NaN;
         var _loc8_:Point = null;
         var _loc9_:Point = null;
         _loc2_ = param1.object;
         var _loc3_:LayoutBounds = getLayoutBounds(_loc2_);
         if(_loc3_)
         {
            _loc4_ = _loc2_.x + _loc3_.pivotX;
            _loc5_ = _loc2_.y + _loc3_.pivotY;
            _loc6_ = _loc3_.width;
            _loc7_ = _loc3_.height;
         }
         else
         {
            _loc4_ = _loc2_.x;
            _loc5_ = _loc2_.y;
            _loc6_ = _loc2_.width;
            _loc7_ = _loc2_.height;
         }
         if(_loc2_.parent)
         {
            _loc8_ = _loc2_.parent.localToGlobal(new Point(_loc4_,_loc5_));
            _loc9_ = _loc2_.parent.localToGlobal(new Point(_loc4_ + _loc6_,_loc5_ + _loc7_));
         }
         else
         {
            _loc8_ = new Point(_loc4_,_loc5_);
            _loc9_ = new Point(_loc4_ + _loc6_,_loc5_ + _loc7_);
         }
         var _loc10_:Number = _loc9_.x - _loc8_.x;
         var _loc11_:Number = _loc9_.y - _loc8_.y;
         if(param1.config)
         {
            param1.config.x = _loc8_.x;
            param1.config.y = _loc8_.y;
         }
         return {
            "x":_loc8_.x,
            "y":_loc8_.y,
            "width":_loc10_,
            "height":_loc11_
         };
      }
      
      override protected function applyDefaultPosition(param1:DisplayObject, param2:Rectangle) : void
      {
         var _loc3_:Point = Boolean(param1.parent) ? param1.parent.globalToLocal(new Point(param2.x,param2.y)) : new Point(param2.x,param2.y);
         var _loc4_:LayoutBounds = getLayoutBounds(param1);
         if(_loc4_)
         {
            param1.x = _loc3_.x - _loc4_.pivotX;
            param1.y = _loc3_.y - _loc4_.pivotY;
         }
         else
         {
            param1.x = _loc3_.x;
            param1.y = _loc3_.y;
         }
      }
      
      override protected function applyDefaultSize(param1:DisplayObject, param2:Rectangle) : void
      {
         var _loc3_:Number = NaN;
         var _loc4_:Number = NaN;
         var _loc5_:Point = null;
         var _loc6_:Point = null;
         if(param1.parent)
         {
            _loc5_ = param1.parent.globalToLocal(new Point(param2.x,param2.y));
            _loc6_ = param1.parent.globalToLocal(new Point(param2.x + param2.width,param2.y + param2.height));
            _loc3_ = _loc6_.x - _loc5_.x;
            _loc4_ = _loc6_.y - _loc5_.y;
         }
         else
         {
            _loc3_ = param2.width;
            _loc4_ = param2.height;
         }
         if(_loc3_ != param1.width || _loc4_ != param1.height)
         {
            param1.width = _loc3_;
            param1.height = _loc4_;
         }
      }
   }
}
