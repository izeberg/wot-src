package net.wg.gui.battle.views.vehicleMarkers
{
   import flash.display.Sprite;
   import flash.text.TextField;
   import flash.text.TextFieldAutoSize;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   import scaleform.gfx.TextFieldEx;
   
   public class DamageLabel extends Sprite implements IDisposable
   {
       
      
      public var orange:TextField = null;
      
      public var green:TextField = null;
      
      public var red:TextField = null;
      
      public var gold:TextField = null;
      
      public var blue:TextField = null;
      
      public var yellow:TextField = null;
      
      public var purple:TextField = null;
      
      public var white:TextField = null;
      
      private var _currentTF:TextField = null;
      
      protected var tfMap:Object;
      
      private var _disposed:Boolean = false;
      
      public function DamageLabel()
      {
         this.tfMap = {};
         super();
         this._currentTF = this.green;
         this.green.visible = false;
         this.red.visible = false;
         this.gold.visible = false;
         this.blue.visible = false;
         this.orange.visible = false;
         this.yellow.visible = false;
         this.purple.visible = false;
         this.white.visible = false;
         TextFieldEx.setNoTranslate(this.green,true);
         TextFieldEx.setNoTranslate(this.red,true);
         TextFieldEx.setNoTranslate(this.gold,true);
         TextFieldEx.setNoTranslate(this.blue,true);
         TextFieldEx.setNoTranslate(this.orange,true);
         TextFieldEx.setNoTranslate(this.yellow,true);
         TextFieldEx.setNoTranslate(this.purple,true);
         TextFieldEx.setNoTranslate(this.white,true);
         this.tfMap["green"] = this.green;
         this.tfMap["red"] = this.red;
         this.tfMap["gold"] = this.gold;
         this.tfMap["blue"] = this.blue;
         this.tfMap["orange"] = this.orange;
         this.tfMap["yellow"] = this.yellow;
         this.tfMap["purple"] = this.purple;
         this.tfMap["white"] = this.white;
         this.autoSize = TextFieldAutoSize.LEFT;
      }
      
      public function dispose() : void
      {
         this._disposed = true;
         this.green = null;
         this.red = null;
         this.gold = null;
         this.blue = null;
         this.orange = null;
         this.yellow = null;
         this.purple = null;
         this.white = null;
         this._currentTF = null;
         this.tfMap["green"] = null;
         this.tfMap["red"] = null;
         this.tfMap["gold"] = null;
         this.tfMap["blue"] = null;
         this.tfMap["orange"] = null;
         this.tfMap["yellow"] = null;
         this.tfMap["purple"] = null;
         this.tfMap["white"] = null;
         this.tfMap = null;
      }
      
      private function showTF(param1:String) : void
      {
         if(this.tfMap[param1])
         {
            this._currentTF.visible = false;
            this._currentTF = this.tfMap[param1];
            this._currentTF.visible = true;
         }
         else
         {
            App.utils.asserter.assert(false,"Can\'t find TextField " + param1 + " in DamageLabel");
         }
      }
      
      public function set color(param1:String) : void
      {
         this.showTF(param1);
      }
      
      public function set text(param1:String) : void
      {
         if(this._currentTF)
         {
            this._currentTF.text = param1;
         }
      }
      
      public function get textWidth() : Number
      {
         return Boolean(this._currentTF) ? Number(this._currentTF.textWidth) : Number(0);
      }
      
      public function isDisposed() : Boolean
      {
         return this._disposed;
      }
      
      public function set autoSize(param1:String) : void
      {
         var _loc2_:TextField = null;
         switch(param1)
         {
            case TextFieldAutoSize.CENTER:
               for each(_loc2_ in this.tfMap)
               {
                  _loc2_.autoSize = TextFieldAutoSize.CENTER;
                  _loc2_.x = _loc2_.width >> 1;
               }
               break;
            case TextFieldAutoSize.RIGHT:
               for each(_loc2_ in this.tfMap)
               {
                  _loc2_.autoSize = TextFieldAutoSize.RIGHT;
                  _loc2_.x = _loc2_.width;
               }
               break;
            case TextFieldAutoSize.LEFT:
            default:
               for each(_loc2_ in this.tfMap)
               {
                  _loc2_.autoSize = TextFieldAutoSize.LEFT;
                  _loc2_.x = 0;
               }
         }
      }
   }
}
