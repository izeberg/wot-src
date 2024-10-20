package net.wg.gui.lobby.header.headerButtonBar
{
   import flash.display.DisplayObject;
   import flash.geom.Rectangle;
   import flash.text.TextFieldAutoSize;
   import net.wg.data.constants.Directions;
   import net.wg.data.constants.Values;
   import net.wg.data.constants.generated.CURRENCIES_CONSTANTS;
   import net.wg.gui.interfaces.IHeaderButtonResizableItem;
   import net.wg.gui.lobby.header.events.HeaderEvents;
   import net.wg.gui.lobby.header.vo.HeaderButtonVo;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   import net.wg.utils.helpLayout.HelpLayoutVO;
   import net.wg.utils.helpLayout.IHelpLayoutComponent;
   import scaleform.clik.controls.Button;
   import scaleform.clik.controls.ButtonBar;
   import scaleform.clik.interfaces.IDataProvider;
   
   public class HeaderButtonBar extends ButtonBar implements IHelpLayoutComponent
   {
      
      private static const HELP_LAYOUT_ID_DELIMITER:String = "_";
      
      private static const SHIFT_X:int = 3;
      
      private static const SHIFT_Y:int = 2;
       
      
      private var _currentScreen:String = "";
      
      private var _screenWidth:int;
      
      private var _wideScreenPrc:Number = 0;
      
      private var _maxScreenPrc:Number = 0;
      
      private var _centerItemNum:int;
      
      private var _centerItemRect:Rectangle = null;
      
      private var _itemsUpdated:int = 0;
      
      private var _firstLeftRightAlignItemIsSet:Boolean = true;
      
      private var _lastRightLeftAlignItem:HeaderButton = null;
      
      private var _helpLayoutId:String = "";
      
      public function HeaderButtonBar()
      {
         super();
      }
      
      override protected function configUI() : void
      {
         visible = false;
         super.configUI();
         App.utils.helpLayout.registerComponent(this);
      }
      
      override protected function updateRenderers() : void
      {
         var _loc4_:int = 0;
         var _loc5_:Button = null;
         var _loc6_:Boolean = false;
         var _loc1_:DisplayObject = null;
         if(_renderers[0] is Class(_itemRendererClass))
         {
            while(_renderers.length > _dataProvider.length)
            {
               _loc4_ = _renderers.length - 1;
               if(container.contains(_renderers[_loc4_]))
               {
                  _loc1_ = _renderers[_loc4_];
                  container.removeChild(_loc1_);
                  this.removeRenderer(_loc1_);
               }
               _renderers.splice(_loc4_--,1);
            }
         }
         else
         {
            while(container.numChildren > 0)
            {
               _loc1_ = container.removeChildAt(0);
               this.removeRenderer(_loc1_);
            }
            _renderers.length = 0;
         }
         this._firstLeftRightAlignItemIsSet = true;
         this._lastRightLeftAlignItem = null;
         var _loc2_:int = _dataProvider.length;
         var _loc3_:uint = 0;
         while(_loc3_ < _loc2_)
         {
            _loc6_ = false;
            if(_loc3_ < _renderers.length)
            {
               _loc5_ = _renderers[_loc3_];
            }
            else
            {
               _loc5_ = Button(App.utils.classFactory.getComponent(_itemRenderer,Button));
               this.setupRenderer(_loc5_,_loc3_);
               _loc6_ = true;
            }
            this.populateRendererData(_loc5_,_loc3_);
            _loc5_.validateNow();
            if(_loc6_ && _loc5_ != null)
            {
               _loc5_.group = _group;
               container.addChild(_loc5_);
               _renderers.push(_loc5_);
               if(this._currentScreen != Values.EMPTY_STR)
               {
                  this.updateRendererScreen(_loc5_);
               }
            }
            _loc3_++;
         }
         if(this._centerItemNum < 0)
         {
            this._centerItemNum = _dataProvider.length;
         }
         App.tutorialMgr.dispatchEventForCustomComponent(this);
      }
      
      override protected function setupRenderer(param1:Button, param2:uint) : void
      {
         param1.owner = this;
         param1.focusable = false;
         param1.focusTarget = this;
         param1.toggle = false;
         param1.allowDeselect = false;
         param1.addEventListener(HeaderEvents.HBC_SIZE_UPDATED,this.onRendererHbcSizeUpdatedHandler);
      }
      
      override protected function populateRendererData(param1:Button, param2:uint) : void
      {
         var _loc3_:HeaderButton = HeaderButton(param1);
         var _loc4_:HeaderButtonVo = HeaderButtonVo(dataProvider.requestItemAt(param2));
         if(_loc4_.direction == TextFieldAutoSize.RIGHT && this._centerItemNum == -1)
         {
            this._centerItemNum = param2;
         }
         var _loc5_:Boolean = true;
         if(_loc4_.direction == TextFieldAutoSize.LEFT && _loc4_.align == TextFieldAutoSize.LEFT)
         {
            _loc5_ = true;
         }
         else if(_loc4_.direction == TextFieldAutoSize.LEFT && _loc4_.align == TextFieldAutoSize.RIGHT && this._firstLeftRightAlignItemIsSet)
         {
            this._firstLeftRightAlignItemIsSet = false;
            _loc5_ = false;
         }
         else if(_loc4_.direction == TextFieldAutoSize.RIGHT && _loc4_.align == TextFieldAutoSize.LEFT)
         {
            this._lastRightLeftAlignItem = _loc3_;
         }
         else if(_loc4_.direction == TextFieldAutoSize.RIGHT && _loc4_.align == TextFieldAutoSize.RIGHT)
         {
            _loc5_ = true;
            if(this._lastRightLeftAlignItem)
            {
               this._lastRightLeftAlignItem.isShowSeparator = false;
            }
         }
         _loc3_.isShowSeparator = _loc5_;
         _loc3_.data = _loc4_;
      }
      
      override protected function onDispose() : void
      {
         var _loc1_:DisplayObject = null;
         while(container.numChildren > 0)
         {
            _loc1_ = container.removeChildAt(0);
            this.removeRenderer(_loc1_);
         }
         _renderers.length = 0;
         _renderers = null;
         this._lastRightLeftAlignItem = null;
         this._centerItemRect = null;
         super.onDispose();
      }
      
      public function getLayoutProperties() : Vector.<HelpLayoutVO>
      {
         var _loc9_:int = 0;
         var _loc10_:int = 0;
         var _loc11_:HeaderButtonVo = null;
         var _loc12_:HeaderButton = null;
         var _loc1_:int = 0;
         var _loc2_:int = 0;
         var _loc3_:Array = [CURRENCIES_CONSTANTS.CRYSTAL,CURRENCIES_CONSTANTS.GOLD,CURRENCIES_CONSTANTS.CREDITS,CURRENCIES_CONSTANTS.FREE_XP];
         var _loc4_:HeaderButton = null;
         var _loc5_:HeaderButton = null;
         var _loc6_:HeaderButton = null;
         var _loc7_:HeaderButton = null;
         if(_renderers && _renderers.length > 0)
         {
            _loc9_ = _renderers.length;
            _loc10_ = 0;
            while(_loc10_ < _loc9_)
            {
               _loc11_ = HeaderButtonVo(dataProvider.requestItemAt(_loc10_));
               if(_loc3_.indexOf(_loc11_.id) > -1)
               {
                  _loc12_ = this.getRendererAt(_loc10_);
                  if(_loc4_)
                  {
                     if(_loc12_.x < _loc4_.x)
                     {
                        _loc4_ = _loc12_;
                     }
                  }
                  else
                  {
                     _loc4_ = _loc12_;
                  }
                  if(_loc5_)
                  {
                     if(_loc12_.x > _loc5_.x)
                     {
                        _loc5_ = _loc12_;
                     }
                  }
                  else
                  {
                     _loc5_ = _loc12_;
                  }
                  if(_loc6_)
                  {
                     if(_loc12_.y < _loc6_.y)
                     {
                        _loc6_ = _loc12_;
                     }
                  }
                  else
                  {
                     _loc6_ = _loc12_;
                  }
                  if(_loc7_)
                  {
                     if(_loc12_.y > _loc7_.y)
                     {
                        _loc7_ = _loc12_;
                     }
                  }
                  else
                  {
                     _loc7_ = _loc12_;
                  }
               }
               _loc10_++;
            }
            _loc1_ = _loc5_.x + _loc5_.bounds.width - _loc4_.x;
            _loc2_ = _loc7_.y + _loc7_.bounds.height - _loc6_.y;
         }
         if(!this._helpLayoutId)
         {
            this._helpLayoutId = name + HELP_LAYOUT_ID_DELIMITER + Math.random();
         }
         var _loc8_:HelpLayoutVO = new HelpLayoutVO();
         _loc8_.x = SHIFT_X;
         _loc8_.y = SHIFT_Y;
         _loc8_.width = _loc1_ - SHIFT_X;
         _loc8_.height = _loc2_ - SHIFT_Y * 2;
         _loc8_.extensibilityDirection = Directions.RIGHT;
         _loc8_.message = LOBBY_HELP.HEADER_FINANCE_BLOCK;
         _loc8_.id = this._helpLayoutId;
         _loc8_.scope = _loc4_;
         return new <HelpLayoutVO>[_loc8_];
      }
      
      public function getRendererAt(param1:uint, param2:int = 0) : HeaderButton
      {
         if(_renderers == null)
         {
            return null;
         }
         var _loc3_:uint = param1 - param2;
         if(_loc3_ >= _renderers.length)
         {
            return null;
         }
         return _renderers[_loc3_] as HeaderButton;
      }
      
      public function updateCenterItem(param1:Rectangle) : void
      {
         this._centerItemRect = param1;
      }
      
      public function updateScreen(param1:String, param2:Number, param3:Number, param4:Number) : void
      {
         var _loc5_:int = 0;
         var _loc6_:int = 0;
         this._screenWidth = param2;
         if(this._currentScreen != param1 || this._wideScreenPrc != param3 || this._maxScreenPrc != param4)
         {
            this._wideScreenPrc = param3;
            this._maxScreenPrc = param4;
            this._currentScreen = param1;
            this._itemsUpdated = 0;
            if(_renderers && _renderers.length > 0)
            {
               _loc5_ = _renderers.length;
               _loc6_ = 0;
               while(_loc6_ < _loc5_)
               {
                  this.updateRendererScreen(_renderers[_loc6_]);
                  _loc6_++;
               }
            }
         }
         this.repositionItems();
      }
      
      private function removeRenderer(param1:DisplayObject) : void
      {
         if(param1 is IDisposable)
         {
            IDisposable(param1).dispose();
         }
         param1.removeEventListener(HeaderEvents.HBC_SIZE_UPDATED,this.onRendererHbcSizeUpdatedHandler);
         param1 = null;
      }
      
      private function repositionItems() : void
      {
         var _loc1_:HeaderButton = null;
         var _loc2_:HeaderButtonVo = null;
         var _loc3_:int = 0;
         var _loc4_:int = 0;
         var _loc5_:int = 0;
         if(_renderers && _renderers.length > 0)
         {
            if(this._itemsUpdated < _renderers.length || this._centerItemNum == -1)
            {
               return;
            }
            _loc3_ = 0;
            _loc4_ = 0;
            _loc5_ = _renderers.length;
            _loc3_ = 0;
            while(_loc3_ < _loc5_ && _loc3_ < this._centerItemNum)
            {
               _loc1_ = _renderers[_loc3_];
               if(_loc1_.isReadyToShow)
               {
                  _loc2_ = _loc1_.headerButtonData;
                  if(!(_loc2_.direction == TextFieldAutoSize.LEFT && _loc2_.align == TextFieldAutoSize.LEFT))
                  {
                     break;
                  }
                  _loc1_.x = _loc4_;
                  _loc4_ += _loc1_.bounds.width;
               }
               _loc3_++;
            }
            _loc4_ = this._centerItemRect.x;
            _loc3_ = this._centerItemNum - 1;
            while(_loc3_ >= 0)
            {
               _loc1_ = _renderers[_loc3_];
               if(_loc1_.isReadyToShow)
               {
                  _loc2_ = _loc1_.headerButtonData;
                  if(!(_loc2_.direction == TextFieldAutoSize.LEFT && _loc2_.align == TextFieldAutoSize.RIGHT))
                  {
                     break;
                  }
                  _loc4_ -= _loc1_.bounds.width;
                  _loc1_.x = _loc4_;
               }
               _loc3_--;
            }
            _loc4_ = this._screenWidth;
            _loc3_ = _loc5_ - 1;
            while(_loc3_ >= this._centerItemNum)
            {
               _loc1_ = _renderers[_loc3_];
               if(_loc1_.isReadyToShow)
               {
                  _loc2_ = _loc1_.headerButtonData;
                  if(!(_loc2_.direction == TextFieldAutoSize.RIGHT && _loc2_.align == TextFieldAutoSize.RIGHT))
                  {
                     break;
                  }
                  _loc4_ += -_loc1_.bounds.width;
                  _loc1_.x = _loc4_;
               }
               _loc3_--;
            }
            _loc4_ = this._centerItemRect.x + this._centerItemRect.width;
            _loc3_ = this._centerItemNum;
            while(_loc3_ < _loc5_)
            {
               _loc1_ = _renderers[_loc3_];
               if(_loc1_.isReadyToShow)
               {
                  _loc2_ = _loc1_.headerButtonData;
                  if(!(_loc2_.direction == TextFieldAutoSize.RIGHT && _loc2_.align == TextFieldAutoSize.LEFT))
                  {
                     break;
                  }
                  _loc1_.x = _loc4_;
                  _loc4_ += _loc1_.bounds.width;
               }
               _loc3_++;
            }
         }
         this.updateFreeSizeButtons();
         dispatchEvent(new HeaderEvents(HeaderEvents.HEADER_ITEMS_REPOSITION,this._screenWidth));
      }
      
      private function updateFreeSizeButtons() : void
      {
         var _loc5_:HeaderButtonVo = null;
         var _loc11_:int = 0;
         var _loc12_:Number = NaN;
         var _loc13_:IHeaderButtonResizableItem = null;
         var _loc14_:int = 0;
         if(!_renderers || _renderers.length == 0)
         {
            return;
         }
         var _loc1_:HeaderButton = null;
         var _loc2_:HeaderButton = null;
         var _loc3_:Vector.<IHeaderButtonResizableItem> = new Vector.<IHeaderButtonResizableItem>();
         var _loc4_:Vector.<int> = new Vector.<int>();
         var _loc6_:int = 0;
         var _loc7_:int = 0;
         var _loc8_:int = _renderers.length;
         var _loc9_:int = 0;
         while(_loc9_ < _loc8_)
         {
            _loc1_ = _renderers[_loc9_];
            _loc5_ = _loc1_.headerButtonData;
            if(_loc5_ && _loc5_.resizePriority > 0)
            {
               if(_loc5_.direction == TextFieldAutoSize.LEFT)
               {
                  if(!_loc2_)
                  {
                     _loc2_ = _loc1_;
                  }
               }
               else if(_loc5_.direction == TextFieldAutoSize.RIGHT)
               {
                  _loc11_ = 0;
                  while(_loc11_ < _loc4_.length)
                  {
                     if(_loc5_.resizePriority <= _loc4_[_loc11_])
                     {
                        break;
                     }
                     _loc11_++;
                  }
                  _loc4_.splice(_loc11_,0,_loc5_.resizePriority);
                  _loc3_.splice(_loc11_,0,_loc1_.content);
               }
            }
            else if(_loc5_.direction == TextFieldAutoSize.LEFT)
            {
               _loc6_ += _loc1_.bounds.width;
            }
            else
            {
               _loc7_ += _loc1_.bounds.width;
            }
            _loc9_++;
         }
         if(_loc2_)
         {
            _loc6_ = this._centerItemRect.x - _loc6_;
            _loc2_.content.setAvailableWidth(_loc6_);
         }
         var _loc10_:uint = _loc3_.length;
         if(_loc10_ > 0)
         {
            _loc7_ = this._screenWidth - (this._centerItemRect.x + this._centerItemRect.width + _loc7_);
            _loc9_ = 0;
            while(_loc9_ < _loc10_)
            {
               _loc12_ = 0;
               _loc14_ = _loc9_ + 1;
               while(_loc14_ < _loc10_)
               {
                  _loc12_ += _loc3_[_loc14_].getMinAvailableWidth();
                  _loc14_++;
               }
               _loc13_ = _loc3_[_loc9_];
               _loc13_.setAvailableWidth(_loc7_ - _loc12_);
               _loc7_ -= _loc13_.getActualWidth();
               _loc9_++;
            }
         }
      }
      
      private function updateRendererScreen(param1:Button) : void
      {
         HeaderButton(param1).updateScreen(this._currentScreen,this._wideScreenPrc,this._maxScreenPrc);
      }
      
      override public function set dataProvider(param1:IDataProvider) : void
      {
         this._itemsUpdated = 0;
         this._centerItemNum = -1;
         super.dataProvider = param1;
      }
      
      private function onRendererHbcSizeUpdatedHandler(param1:HeaderEvents) : void
      {
         if(this._itemsUpdated < _renderers.length)
         {
            ++this._itemsUpdated;
         }
         if(this._itemsUpdated >= _renderers.length && !visible)
         {
            visible = true;
         }
         this.repositionItems();
      }
   }
}
