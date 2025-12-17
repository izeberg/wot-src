package net.wg.gui.lobby.vehicleCustomization.controls.bottomPanel
{
   import flash.display.Sprite;
   import flash.geom.Point;
   import flash.text.TextField;
   import flash.text.TextFieldAutoSize;
   import mx.effects.easing.Linear;
   import net.wg.infrastructure.base.UIComponentEx;
   import net.wg.infrastructure.interfaces.entity.IUpdatable;
   import scaleform.clik.motion.Tween;
   
   public class CustomizationModalLine extends UIComponentEx implements IUpdatable
   {
       
      
      public var value:TextField = null;
      
      public var left:Sprite = null;
      
      public var right:Sprite = null;
      
      private var _tweens:Vector.<Tween>;
      
      private const ANIMATION_DURATION:int = 300;
      
      private const ANIMATION_TEXT_OFFSET:int = 4;
      
      private const MIN_LINE_SIZE:int = 15;
      
      private const OFFSET:int = 5;
      
      public function CustomizationModalLine()
      {
         this._tweens = new Vector.<Tween>();
         super();
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this.value.autoSize = TextFieldAutoSize.LEFT;
         this.value.text = VEHICLE_CUSTOMIZATION.CUSTOMIZATION_MODELINE_TITLE;
      }
      
      public function update(param1:Object) : void
      {
         var _loc2_:Point = null;
         _loc2_ = Point(param1);
         var _loc3_:int = _loc2_.y - _loc2_.x;
         var _loc4_:int = (_loc3_ - this.value.width) / 2 | 0;
         this.left.x = 0;
         this.clearTweens();
         this._tweens.push(new Tween(this.ANIMATION_DURATION,this.value,{"x":_loc4_ + this.ANIMATION_TEXT_OFFSET},{"ease":Linear.easeIn}));
         this._tweens.push(new Tween(this.ANIMATION_DURATION,this,{"alpha":Number(_loc2_.x != _loc2_.y)},{"ease":Linear.easeIn}));
         this._tweens.push(new Tween(this.ANIMATION_DURATION,this.left,{
            "x":_loc4_ - Math.max(this.MIN_LINE_SIZE,_loc4_),
            "width":Math.max(this.MIN_LINE_SIZE,_loc4_)
         },{"ease":Linear.easeIn}));
         this._tweens.push(new Tween(this.ANIMATION_DURATION,this.right,{
            "x":_loc4_ + this.value.width + this.OFFSET,
            "width":Math.max(this.MIN_LINE_SIZE,_loc3_ - (_loc4_ + this.value.width))
         },{"ease":Linear.easeIn}));
      }
      
      public function clearTweens() : void
      {
         var _loc1_:Tween = null;
         if(this._tweens.length > 0)
         {
            for each(_loc1_ in this._tweens)
            {
               _loc1_.dispose();
               _loc1_ = null;
            }
            this._tweens.length = 0;
         }
      }
      
      override protected function onDispose() : void
      {
         this.clearTweens();
         this._tweens = null;
         super.onDispose();
      }
   }
}
