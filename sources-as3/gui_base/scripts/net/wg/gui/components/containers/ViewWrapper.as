package net.wg.gui.components.containers
{
   import flash.display.Bitmap;
   import flash.display.BitmapData;
   import flash.display.DisplayObject;
   import flash.display.InteractiveObject;
   import flash.display.Sprite;
   import flash.events.Event;
   import flash.geom.Matrix;
   import flash.geom.Point;
   import flash.geom.Rectangle;
   import flash.text.TextField;
   import flash.text.TextFieldType;
   import flash.text.TextFormat;
   import net.wg.gui.tutorial.components.TutorialHintZone;
   import net.wg.infrastructure.events.ExternalCursorEvent;
   import net.wg.utils.StaticUtils;
   import scaleform.gfx.TextFieldEx;
   
   public class ViewWrapper extends BaseWrapper
   {
      
      private static var _debugMode:uint = 0;
      
      private static const HIT_AREA_SPRITE:String = "hitAreaSprite";
       
      
      private var _inputTF:TextField = null;
      
      private var _bitmap:Bitmap = null;
      
      private var _debugSprite:Sprite = null;
      
      private var _hitAreaTopLeft:Point;
      
      private var _hitAreaBottomRight:Point;
      
      private var _width:uint = 0;
      
      private var _height:uint = 0;
      
      private var _cursor:String = "arrow";
      
      public function ViewWrapper()
      {
         super();
         this._hitAreaTopLeft = new Point();
         this._hitAreaBottomRight = new Point();
         this.addGFBitmap();
         this.addInputTF();
         this.addHitArea();
         mouseEnabled = true;
         tabChildren = false;
         tabEnabled = true;
         App.cursor.registerExternalComponent(this,this._cursor);
      }
      
      override public function caretPosChanged(param1:Number, param2:Number) : void
      {
         App.utils.asserter.assert(contains(this._inputTF),"_inputTF must be on stage during text input");
         var _loc3_:Number = this._inputTF.x;
         this._inputTF.x = param1 - this._inputTF.textWidth;
         this._inputTF.y = param2;
         this._inputTF.width -= this._inputTF.x - _loc3_;
      }
      
      override public function dispose() : void
      {
         App.cursor.unregisterExternalComponent(this);
         if(this._bitmap.bitmapData)
         {
            this._bitmap.bitmapData.dispose();
            this._bitmap.bitmapData = null;
         }
         this._bitmap = null;
         this._inputTF = null;
         this._hitAreaTopLeft = null;
         this._hitAreaBottomRight = null;
         this._debugSprite = null;
         removeChild(hitArea);
         hitArea = null;
         super.dispose();
      }
      
      override public function freezeUntilResize() : void
      {
         this._bitmap.cacheAsBitmap = true;
      }
      
      override public function getComponentForFocus() : InteractiveObject
      {
         return Boolean(this._inputTF.stage) ? this._inputTF : this;
      }
      
      override public function inputEnded() : void
      {
         var _loc1_:InteractiveObject = App.utils.focusHandler.getFocus(0);
         if(_loc1_ == this._inputTF)
         {
            App.utils.focusHandler.setFocus(this);
         }
         this._inputTF.text = "";
         removeChild(this._inputTF);
      }
      
      override public function inputStarted(param1:Number, param2:Number, param3:Number, param4:Number) : void
      {
         addChild(this._inputTF);
         this._inputTF.x = param1;
         this._inputTF.y = param2;
         this._inputTF.width = param3;
         this._inputTF.height = param4;
         var _loc5_:InteractiveObject = App.utils.focusHandler.getFocus(0);
         if(_loc5_ == this)
         {
            App.utils.focusHandler.setFocus(this._inputTF);
         }
      }
      
      override public function setCursor(param1:String) : void
      {
         if(this._cursor == param1)
         {
            return;
         }
         this._cursor = param1;
         dispatchEvent(new ExternalCursorEvent(this._cursor));
      }
      
      override public function setHitAreaPaddings(param1:int, param2:int, param3:int, param4:int) : void
      {
         this._hitAreaTopLeft.x = param4;
         this._hitAreaTopLeft.y = param1;
         this._hitAreaBottomRight.x = param2;
         this._hitAreaBottomRight.y = param3;
         this.updateHitArea();
         this.updateDebugGraphics();
         dispatchEvent(new Event(Event.RESIZE));
      }
      
      override public function setScale(param1:Number) : void
      {
         scaleX = scaleY = param1;
      }
      
      override public function setSize(param1:uint, param2:uint) : void
      {
         this._width = param1;
         this._height = param2;
         if(this._bitmap.bitmapData)
         {
            this._bitmap.width = param1;
            this._bitmap.height = param2;
         }
         this.updateHitArea();
         this.updateDebugGraphics();
         dispatchEvent(new Event(Event.RESIZE));
      }
      
      override public function setTexture(param1:BitmapData) : void
      {
         var _loc2_:BitmapData = this._bitmap.bitmapData;
         this._bitmap.cacheAsBitmap = false;
         this._bitmap.bitmapData = param1;
         this._bitmap.width = this._width;
         this._bitmap.height = this._height;
         if(_loc2_)
         {
            _loc2_.dispose();
         }
      }
      
      override protected function focusChanged(param1:Boolean) : void
      {
         this.updateDebugGraphics();
      }
      
      private function updateHitArea() : void
      {
         var _loc1_:int = this._width - (this._hitAreaTopLeft.x + this._hitAreaBottomRight.x) / scaleX | 0;
         var _loc2_:int = this._height - (this._hitAreaTopLeft.y + this._hitAreaBottomRight.y) / scaleY | 0;
         var _loc3_:int = this._hitAreaTopLeft.x / scaleX | 0;
         var _loc4_:int = this._hitAreaTopLeft.y / scaleY | 0;
         _loc1_ = Math.max(_loc1_,0);
         _loc2_ = Math.max(_loc2_,0);
         _loc3_ = _loc3_ + _loc1_ > this._width ? int(0) : int(_loc3_);
         _loc4_ = _loc4_ + _loc2_ > this._height ? int(0) : int(_loc4_);
         hitArea.x = _loc3_;
         hitArea.y = _loc4_;
         hitArea.width = _loc1_;
         hitArea.height = _loc2_;
      }
      
      private function updateDebugGraphics() : void
      {
         var _loc1_:TutorialHintZone = null;
         if(_debugMode == 0)
         {
            this._inputTF.alpha = 0;
            graphics.clear();
            if(this._debugSprite)
            {
               removeChild(this._debugSprite);
               this._debugSprite = null;
            }
            return;
         }
         if(_debugMode == 1)
         {
            this._inputTF.alpha = 0;
            graphics.clear();
            if(!this._debugSprite)
            {
               addChildAt(this._debugSprite = new Sprite(),getChildIndex(this._bitmap) + 1);
               this._debugSprite.mouseEnabled = false;
            }
            this._debugSprite.graphics.clear();
            this.drawCross(this,20,StaticUtils.number2Color(StaticUtils.string2Hash(name)),0.7);
            return;
         }
         if(this._width == 0 || this._height == 0)
         {
            return;
         }
         if(!this._debugSprite)
         {
            addChildAt(this._debugSprite = new Sprite(),getChildIndex(this._bitmap) + 1);
            this._debugSprite.mouseEnabled = false;
         }
         this._inputTF.alpha = 1;
         graphics.clear();
         graphics.beginFill(16776960,0.1);
         graphics.drawRect(0,0,this._width,this._height);
         graphics.endFill();
         this._debugSprite.graphics.clear();
         this.drawBorder(hitArea,3,255,0.5);
         if(focused)
         {
            this.drawBorder(hitArea,5,16777215,0.5);
         }
         for each(_loc1_ in _tutorialHintZones)
         {
            this.drawBorder(_loc1_,3,16711680,0.5);
            this.drawLabel(_loc1_,_loc1_.name);
         }
      }
      
      private function drawBorder(param1:DisplayObject, param2:Number, param3:uint, param4:Number) : void
      {
         if(param1.width > 0 && param1.height > 0)
         {
            this._debugSprite.graphics.lineStyle(param2,param3,param4);
            this._debugSprite.graphics.drawRect(param1.x,param1.y,param1.width,param1.height);
            this._debugSprite.graphics.lineStyle();
         }
      }
      
      private function drawCross(param1:DisplayObject, param2:Number, param3:uint, param4:Number) : void
      {
         var _loc5_:uint = param2 >> 1;
         if(param1.width > 0 && param1.height > 0)
         {
            this._debugSprite.graphics.lineStyle(param2,param3,param4);
            this._debugSprite.graphics.moveTo(_loc5_,_loc5_);
            this._debugSprite.graphics.lineTo(param1.width - _loc5_,param1.height - _loc5_);
            this._debugSprite.graphics.moveTo(_loc5_,param1.height - _loc5_);
            this._debugSprite.graphics.lineTo(param1.width - _loc5_,_loc5_);
            this._debugSprite.graphics.lineTo(param1.width - _loc5_,param1.height - _loc5_);
            this._debugSprite.graphics.lineTo(_loc5_,param1.height - _loc5_);
            this._debugSprite.graphics.lineTo(_loc5_,_loc5_);
            this._debugSprite.graphics.lineTo(param1.width - _loc5_,_loc5_);
            this._debugSprite.graphics.lineStyle();
         }
      }
      
      private function drawLabel(param1:DisplayObject, param2:String) : void
      {
         var _loc4_:TextField = null;
         var _loc3_:TextFormat = new TextFormat();
         _loc3_.font = "$FieldFont";
         _loc3_.size = 14;
         _loc3_.color = 16711680;
         _loc4_ = new TextField();
         _loc4_.text = param2;
         _loc4_.setTextFormat(_loc3_);
         App.utils.commons.updateTextFieldSize(_loc4_);
         var _loc5_:uint = param1.x + (param1.width >> 1) - (_loc4_.width >> 1);
         var _loc6_:uint = param1.y - _loc4_.height;
         var _loc7_:BitmapData = new BitmapData(_loc4_.width,_loc4_.height,true,0);
         _loc7_.draw(_loc4_);
         var _loc8_:Matrix = new Matrix();
         _loc8_.translate(_loc5_,_loc6_);
         this._debugSprite.graphics.beginBitmapFill(_loc7_,_loc8_,false,true);
         this._debugSprite.graphics.drawRect(_loc5_,_loc6_,_loc4_.width,_loc4_.height);
         this._debugSprite.graphics.endFill();
      }
      
      private function addGFBitmap() : void
      {
         addChild(this._bitmap = new Bitmap());
      }
      
      private function addInputTF() : void
      {
         this._inputTF = new TextField();
         this._inputTF.maxChars = 1;
         this._inputTF.alpha = 0;
         this._inputTF.type = TextFieldType.INPUT;
         this._inputTF.selectable = false;
         this._inputTF.borderColor = 65280;
         this._inputTF.border = true;
         TextFieldEx.setNoTranslate(this._inputTF,true);
      }
      
      private function addHitArea() : void
      {
         var _loc1_:Sprite = new Sprite();
         _loc1_.name = HIT_AREA_SPRITE;
         _loc1_.graphics.clear();
         _loc1_.graphics.beginFill(16711680,0);
         _loc1_.graphics.drawRect(0,0,1,1);
         _loc1_.graphics.endFill();
         addChild(_loc1_);
         hitArea = _loc1_;
      }
      
      override public function get hitRect() : Rectangle
      {
         return new Rectangle(hitArea.x * scaleX,hitArea.y * scaleY,hitArea.width * scaleX,hitArea.height * scaleY);
      }
      
      override public function get debugMode() : uint
      {
         return _debugMode;
      }
      
      override public function set debugMode(param1:uint) : void
      {
         _debugMode = param1;
         this.updateDebugGraphics();
      }
      
      override public function get width() : Number
      {
         return this._width * scaleX;
      }
      
      override public function set width(param1:Number) : void
      {
         this.setSize(param1 / scaleX,this._height);
      }
      
      override public function get height() : Number
      {
         return this._height * scaleY;
      }
      
      override public function set height(param1:Number) : void
      {
         this.setSize(this._width,param1 / scaleY);
      }
   }
}
