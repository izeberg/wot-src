package net.wg.gui.battle.views.widgetsPanel.common
{
   import flash.display.DisplayObjectContainer;
   import flash.utils.Dictionary;
   import net.wg.data.constants.Linkages;
   import net.wg.data.constants.Values;
   import net.wg.gui.battle.views.widgetsPanel.vo.HotKeyVo;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   
   public class HotkeyManager implements IDisposable
   {
       
      
      private var _target:DisplayObjectContainer = null;
      
      private var _settings:HotkeySettings = null;
      
      private var _visible:Boolean = false;
      
      private var _state:String = "normal";
      
      private var _hotKeys:Dictionary;
      
      private var _hotKeysOrder:Vector.<String> = null;
      
      private var _keyCodes:Vector.<HotKeyVo> = null;
      
      private var _isAvailable:Boolean = true;
      
      private var _isDisposed:Boolean = false;
      
      public function HotkeyManager(param1:DisplayObjectContainer, param2:HotkeySettings)
      {
         this._hotKeys = new Dictionary();
         super();
         this._target = param1;
         this._settings = param2;
      }
      
      protected function onDispose() : void
      {
         if(this._hotKeys)
         {
            App.utils.data.cleanupDynamicObject(this._hotKeys);
            this._hotKeys = null;
         }
         if(this._keyCodes)
         {
            App.utils.data.cleanupDynamicObject(this._keyCodes);
            this._keyCodes = null;
         }
         if(this._hotKeysOrder)
         {
            App.utils.data.cleanupDynamicObject(this._hotKeysOrder);
            this._hotKeysOrder = null;
         }
         this._target = null;
         this._settings.dispose();
         this._settings = null;
      }
      
      public final function dispose() : void
      {
         if(this._isDisposed)
         {
            return;
         }
         this.onDispose();
         this._isDisposed = true;
      }
      
      public final function isDisposed() : Boolean
      {
         return this._isDisposed;
      }
      
      public function activateKey(param1:String, param2:Number) : void
      {
         if(!this._isAvailable && this.getHotKey(param1).isLongKey)
         {
            return;
         }
         this.onKeyPress(param1,Values.ZERO);
         this.hideOtherKeys(param1);
         this.hideKey(param1,param2);
      }
      
      public function hideKey(param1:String, param2:Number) : void
      {
         if(!this._isAvailable)
         {
            return;
         }
         var _loc3_:Hotkey = this.getHotKey(param1);
         if(_loc3_)
         {
            _loc3_.hide(param2);
         }
      }
      
      public function hideOtherKeys(param1:String) : void
      {
         var _loc2_:Hotkey = null;
         if(!this._isAvailable)
         {
            return;
         }
         for each(_loc2_ in this._hotKeys)
         {
            if(_loc2_.command != param1)
            {
               _loc2_.hide(Values.ZERO);
            }
         }
      }
      
      public function invalidate() : void
      {
         if(!this._keyCodes)
         {
            return;
         }
         this.updateHotKeys();
         this.updateState(this._state);
         this.updateVisibility(this._visible);
      }
      
      public function onKeyPress(param1:String, param2:Number) : void
      {
         var _loc3_:Hotkey = this.getHotKey(param1);
         if(_loc3_)
         {
            if(this._isAvailable)
            {
               _loc3_.onPress(param2);
            }
            else
            {
               _loc3_.shake();
            }
         }
      }
      
      public function onKeyRelease(param1:String) : void
      {
         if(!this._isAvailable)
         {
            return;
         }
         var _loc2_:Hotkey = this.getHotKey(param1);
         if(_loc2_)
         {
            _loc2_.onRelease();
         }
      }
      
      public function setAvailability(param1:Boolean) : void
      {
         var _loc2_:Hotkey = null;
         if(this._isAvailable == param1)
         {
            return;
         }
         this._isAvailable = param1;
         if(!param1)
         {
            for each(_loc2_ in this._hotKeys)
            {
               if(_loc2_.isInFillTween)
               {
                  _loc2_.onRelease();
               }
            }
         }
      }
      
      public function setData(param1:Vector.<HotKeyVo>) : void
      {
         this._keyCodes = param1;
      }
      
      public function setState(param1:String) : void
      {
         if(this._state == param1)
         {
            return;
         }
         this._state = param1;
         this.updateState(param1);
      }
      
      public function setVisibility(param1:Boolean) : void
      {
         if(this._visible == param1)
         {
            return;
         }
         this._visible = param1;
         this.updateVisibility(param1);
      }
      
      public function shakeKey(param1:String) : void
      {
         var _loc2_:Hotkey = null;
         if(!this._isAvailable)
         {
            _loc2_ = this.getHotKey(param1);
            if(_loc2_)
            {
               _loc2_.shake();
            }
         }
      }
      
      public function showKeys(param1:Number) : void
      {
         var _loc2_:Hotkey = null;
         for each(_loc2_ in this._hotKeys)
         {
            _loc2_.show(param1);
         }
      }
      
      public function hideKeys(param1:Number) : void
      {
         var _loc2_:Hotkey = null;
         for each(_loc2_ in this._hotKeys)
         {
            _loc2_.hide(param1);
         }
      }
      
      private function updateState(param1:String) : void
      {
         var _loc2_:Hotkey = null;
         for each(_loc2_ in this._hotKeys)
         {
            _loc2_.setState(param1);
         }
      }
      
      private function updateVisibility(param1:Boolean) : void
      {
         var _loc2_:Hotkey = null;
         for each(_loc2_ in this._hotKeys)
         {
            _loc2_.visible = param1;
         }
      }
      
      private function updateHotKeys() : void
      {
         var _loc1_:uint = 0;
         var _loc2_:* = null;
         var _loc4_:uint = 0;
         var _loc6_:Hotkey = null;
         var _loc3_:Vector.<String> = new Vector.<String>(0);
         var _loc5_:uint = this._keyCodes.length;
         var _loc7_:uint = Values.ZERO;
         var _loc8_:uint = Values.ZERO;
         this._hotKeysOrder = new Vector.<String>(0);
         _loc1_ = 0;
         while(_loc1_ < _loc5_)
         {
            this._hotKeysOrder.push(this._keyCodes[_loc1_].command);
            _loc1_++;
         }
         for(_loc2_ in this._hotKeys)
         {
            _loc3_.push(_loc2_);
         }
         _loc4_ = _loc3_.length;
         _loc1_ = 0;
         while(_loc1_ < _loc4_)
         {
            _loc2_ = _loc3_[_loc1_];
            if(this._hotKeysOrder.indexOf(_loc2_) == -1)
            {
               _loc6_ = this._hotKeys[_loc2_];
               _loc6_.dispose();
               this._target.removeChild(_loc6_);
               delete this._hotKeys[_loc2_];
            }
            _loc1_++;
         }
         _loc1_ = 0;
         while(_loc1_ < _loc5_)
         {
            _loc2_ = this._keyCodes[_loc1_].command;
            if(this._hotKeys.hasOwnProperty(_loc2_))
            {
               _loc6_ = this._hotKeys[_loc2_];
            }
            else
            {
               _loc6_ = App.utils.classFactory.getComponent(Linkages.WIDGET_HOT_KEY,Hotkey);
               this._hotKeys[_loc2_] = _loc6_;
               this._target.addChild(_loc6_);
            }
            _loc6_.setup(this._keyCodes[_loc1_]);
            _loc6_.visible = this._visible;
            _loc7_ += _loc6_.width;
            _loc8_ += _loc6_.height;
            _loc1_++;
         }
         this._settings.initItemsSize(_loc7_,_loc8_,_loc5_);
         this.updateHotKeysPosition();
      }
      
      private function updateHotKeysPosition() : void
      {
         var _loc2_:String = null;
         var _loc3_:Hotkey = null;
         var _loc1_:uint = this._hotKeysOrder.length;
         var _loc4_:int = this._settings.anchorX;
         var _loc5_:int = this._settings.anchorY;
         var _loc6_:uint = 0;
         while(_loc6_ < _loc1_)
         {
            _loc2_ = this._hotKeysOrder[_loc6_];
            if(this._hotKeys.hasOwnProperty(_loc2_))
            {
               _loc3_ = this._hotKeys[_loc2_];
               _loc3_.setPosition(_loc4_,_loc5_);
               _loc4_ += this._settings.calcHorizontalStep(_loc3_.width);
               _loc5_ += this._settings.calcVerticalStep(_loc3_.height);
            }
            _loc6_++;
         }
      }
      
      private function getHotKey(param1:String) : Hotkey
      {
         return !!this._hotKeys.hasOwnProperty(param1) ? this._hotKeys[param1] : null;
      }
   }
}
