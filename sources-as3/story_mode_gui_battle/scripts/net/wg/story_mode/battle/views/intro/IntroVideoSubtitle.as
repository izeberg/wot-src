package net.wg.story_mode.battle.views.intro
{
   import flash.display.MovieClip;
   import flash.text.TextField;
   import flash.text.TextFieldAutoSize;
   import flash.text.TextFormat;
   import flash.text.TextLineMetrics;
   import net.wg.utils.StageBreakPointList;
   import org.idmedia.as3commons.util.StringUtils;
   
   public class IntroVideoSubtitle extends MovieClip
   {
      
      private static const SIZE_DEFAULT:int = 16;
      
      private static const SIZE_MEDIUM:int = 20;
      
      private static const SIZE_LARGE:int = 24;
      
      private static const BG_COLOR:uint = 0;
      
      private static const BG_ALPHA:Number = 0.2;
      
      private static const CORNERS_RADIUS:uint = 4;
      
      private static const PADDING_TOP:int = 3;
      
      private static const PADDING_RIGHT:int = 10;
      
      private static const PADDING_BOTTOM:int = 7;
      
      private static const PADDING_LEFT:int = 10;
       
      
      public var textField:TextField = null;
      
      public var background:MovieClip = null;
      
      public function IntroVideoSubtitle()
      {
         super();
         this.textField.autoSize = TextFieldAutoSize.LEFT;
      }
      
      public final function dispose() : void
      {
         this.textField = null;
         this.background = null;
      }
      
      public function update(param1:String) : void
      {
         this.textField.text = param1;
         this.textField.visible = StringUtils.isNotEmpty(param1);
         this.updatePosition();
      }
      
      public function updateSize() : void
      {
         this.textField.width = App.appWidth - PADDING_LEFT - PADDING_RIGHT;
         this.updatePosition();
      }
      
      public function updateBreakPoint() : void
      {
         var _loc1_:TextFormat = this.textField.getTextFormat();
         switch(App.stageSizeMgr.currentBreakPoint)
         {
            case StageBreakPointList.MEDIUM:
               _loc1_.size = SIZE_MEDIUM;
               break;
            case StageBreakPointList.LARGE:
            case StageBreakPointList.EXTRA_LARGE:
               _loc1_.size = SIZE_LARGE;
               break;
            default:
               _loc1_.size = SIZE_DEFAULT;
         }
         this.textField.defaultTextFormat = _loc1_;
         this.textField.setTextFormat(_loc1_);
         this.updatePosition();
      }
      
      private function updatePosition() : void
      {
         var _loc1_:TextLineMetrics = null;
         var _loc2_:Number = NaN;
         var _loc3_:uint = 0;
         var _loc4_:uint = 0;
         this.textField.x = -this.textField.width >> 1;
         this.textField.y = -this.textField.height - PADDING_BOTTOM;
         this.background.graphics.clear();
         this.background.cacheAsBitmap = false;
         if(this.textField.visible)
         {
            this.background.x = this.textField.x;
            _loc2_ = this.textField.y;
            _loc3_ = this.textField.numLines;
            _loc4_ = 0;
            while(_loc4_ < _loc3_)
            {
               _loc1_ = this.textField.getLineMetrics(_loc4_);
               this.background.graphics.beginFill(BG_COLOR,BG_ALPHA);
               this.background.graphics.drawRoundRect(_loc1_.x - PADDING_LEFT,_loc2_ - PADDING_TOP,_loc1_.width + PADDING_LEFT + PADDING_RIGHT,_loc1_.height + PADDING_TOP + PADDING_BOTTOM,CORNERS_RADIUS,CORNERS_RADIUS);
               this.background.graphics.endFill();
               _loc2_ += _loc1_.ascent + _loc1_.descent + _loc1_.leading;
               _loc4_++;
            }
         }
         this.background.cacheAsBitmap = true;
      }
   }
}
