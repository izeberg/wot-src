package net.wg.gui.battle.epicBattle.views.upgradePanel
{
   import fl.transitions.easing.Strong;
   import flash.display.BlendMode;
   import flash.display.DisplayObject;
   import flash.display.MovieClip;
   import flash.display.Sprite;
   import flash.events.Event;
   import flash.geom.Point;
   import flash.text.TextField;
   import flash.text.TextFieldAutoSize;
   import net.wg.data.constants.Errors;
   import net.wg.data.constants.generated.BATTLEATLAS;
   import net.wg.gui.battle.components.BattleAtlasSprite;
   import net.wg.gui.battle.epicBattle.views.upgradePanel.data.EpicChoiceInfoPanelVO;
   import net.wg.gui.battle.epicBattle.views.upgradePanel.data.EpicUpgradePanelVO;
   import scaleform.clik.constants.InvalidationType;
   import scaleform.clik.core.UIComponent;
   import scaleform.clik.motion.Tween;
   
   public class EpicChoiceInfoPanel extends UIComponent
   {
      
      public static const SELECT_ANIM_COMPLETE:String = "selectAnimComplete";
      
      private static const BIG_FRAME_LBL:String = "big";
      
      private static const DEFAULT_FRAME_LBL:String = "default";
      
      private static const MODULE_SMALL_OFFSET_X:int = 23;
      
      private static const MODULE_BIG_OFFSET_X:int = 42;
      
      private static const MODULE_ANIM_OFFSET_X:int = 100;
      
      private static const SELECT_ANIM_OFFSET:Point = new Point(39,38);
      
      private static const HIDE_ANIM_ITEMS_OFFSET_Y:int = -20;
      
      private static const NOT_SELECTED_ITEM_ANIM_ALPHA:Number = 0.5;
      
      private static const SHOW_ANIM_DELAY:int = 250;
      
      private static const SHOW_ANIM_DURATION:int = 300;
      
      private static const SHOW_SELECT_DURATION:int = 600;
      
      private static const HIDE_ANIM_DURATION:int = 150;
       
      
      public var firstInfoForSelect:EpicModuleInfo = null;
      
      public var secondInfoForSelect:EpicModuleInfo = null;
      
      public var delimiterTF:TextField = null;
      
      public var delimiter:MovieClip = null;
      
      public var sparks:BattleAtlasSprite = null;
      
      public var light:BattleAtlasSprite = null;
      
      private var _isBig:Boolean = true;
      
      private var _tweens:Vector.<Tween> = null;
      
      private var _selectAnim:Tween = null;
      
      private var _selectAnimContainer:Sprite = null;
      
      private var _leftHitMc:Sprite = null;
      
      private var _rightHitMc:Sprite = null;
      
      private var _availableModules:Vector.<int> = null;
      
      private var _firstItemDefaultX:int = 0;
      
      private var _secondItemDefaultX:int = 0;
      
      private var _delimiterDefaultY:int = 0;
      
      private var _moduleDefaultY:int = 0;
      
      public function EpicChoiceInfoPanel()
      {
         super();
         this._tweens = new Vector.<Tween>(0);
         this._availableModules = new Vector.<int>(0);
         this._selectAnimContainer = new Sprite();
         this.delimiterTF.autoSize = TextFieldAutoSize.LEFT;
         this.sparks.isCentralize = this.light.isCentralize = true;
         this.sparks.imageName = BATTLEATLAS.MODULE_SPARKS;
         this.sparks.blendMode = BlendMode.ADD;
         this.light.imageName = BATTLEATLAS.MODULE_SELECT;
         this._selectAnimContainer.alpha = 0;
         this._selectAnimContainer.addChild(this.light);
         this._selectAnimContainer.addChild(this.sparks);
         this.addChildAt(this._selectAnimContainer,0);
         this._moduleDefaultY = this.firstInfoForSelect.y;
         this._delimiterDefaultY = this.delimiterTF.y;
         App.utils.commons.updateChildrenMouseBehavior(this,false,false,new <DisplayObject>[this.firstInfoForSelect,this.secondInfoForSelect]);
      }
      
      override protected function draw() : void
      {
         super.draw();
         if(isInvalid(InvalidationType.SETTINGS))
         {
            gotoAndStop(!!this._isBig ? BIG_FRAME_LBL : DEFAULT_FRAME_LBL);
            this.setDelimiterText(BATTLE_ROYALE.VEHMODULECONFIGURATOR_DELIMITER);
            this.firstInfoForSelect.initSettings(EpicModuleInfo.TEXT_ORIENTATION_LEFT,this._isBig,0,this._leftHitMc);
            this.secondInfoForSelect.initSettings(EpicModuleInfo.TEXT_ORIENTATION_RIGHT,this._isBig,1,this._rightHitMc);
         }
      }
      
      override protected function onDispose() : void
      {
         this.clearSelectAnim();
         this.clearTweens();
         this.resetAvailableItems();
         this._tweens = null;
         this._availableModules = null;
         this._selectAnimContainer = null;
         this._leftHitMc = null;
         this._rightHitMc = null;
         this.firstInfoForSelect.dispose();
         this.firstInfoForSelect = null;
         this.secondInfoForSelect.dispose();
         this.secondInfoForSelect = null;
         this.delimiterTF = null;
         this.delimiter = null;
         this.sparks = null;
         this.light = null;
         super.onDispose();
      }
      
      public function getModuleInfoMaxBorderSize() : int
      {
         var _loc1_:int = !!this._isBig ? int(MODULE_BIG_OFFSET_X) : int(MODULE_SMALL_OFFSET_X);
         return _loc1_ + Math.max(this.firstInfoForSelect.actualWidth,this.secondInfoForSelect.actualWidth);
      }
      
      public function getModuleInfoMaxHeight() : int
      {
         return Math.max(this.firstInfoForSelect.actualHeight,this.secondInfoForSelect.actualHeight);
      }
      
      public function initSettings(param1:Boolean, param2:Sprite = null, param3:Sprite = null) : void
      {
         this._isBig = param1;
         this._leftHitMc = param2;
         this._rightHitMc = param3;
         invalidate(InvalidationType.SETTINGS);
      }
      
      public function resetAvailableItems() : void
      {
         this._availableModules.splice(0,this._availableModules.length);
      }
      
      public function setData(param1:EpicChoiceInfoPanelVO) : void
      {
         this._availableModules.splice(0,this._availableModules.length);
         if(param1.firstItem != null)
         {
            this.firstInfoForSelect.setData(param1.firstItem);
            this._availableModules.push(this.firstInfoForSelect.intCD);
         }
         if(param1.secondItem != null)
         {
            this.secondInfoForSelect.setData(param1.secondItem);
            this._availableModules.push(this.secondInfoForSelect.intCD);
         }
         this.updatePosition();
      }
      
      public function setDelimiterText(param1:String) : void
      {
         this.delimiterTF.text = param1;
         var _loc2_:int = this.delimiterTF.width;
         this.delimiterTF.x = -_loc2_ >> 1;
      }
      
      public function setDelimiterVisible(param1:Boolean) : void
      {
         this.delimiter.visible = param1;
      }
      
      public function setInitData(param1:EpicUpgradePanelVO) : void
      {
         this.firstInfoForSelect.setHotKeys(param1.firstItem.hotKeysVKeys,param1.firstItem.hotKeys);
         this.secondInfoForSelect.setHotKeys(param1.secondItem.hotKeysVKeys,param1.secondItem.hotKeys);
      }
      
      public function showSelectAnim(param1:int) : void
      {
         var _loc2_:EpicModuleInfo = null;
         this.clearSelectAnim();
         if(param1 == 0)
         {
            this._selectAnimContainer.x = this._firstItemDefaultX - SELECT_ANIM_OFFSET.x;
            this._selectAnimContainer.y = this._moduleDefaultY + SELECT_ANIM_OFFSET.y;
            _loc2_ = this.secondInfoForSelect;
         }
         else if(param1 == 1)
         {
            this._selectAnimContainer.x = this._secondItemDefaultX + SELECT_ANIM_OFFSET.x;
            this._selectAnimContainer.y = this._moduleDefaultY + SELECT_ANIM_OFFSET.y;
            _loc2_ = this.firstInfoForSelect;
         }
         else
         {
            App.utils.asserter.assert(false,Errors.WRONG_VALUE + " idx = " + param1);
         }
         this._tweens.push(new Tween(HIDE_ANIM_DURATION,_loc2_,{"alpha":NOT_SELECTED_ITEM_ANIM_ALPHA}));
         this._selectAnimContainer.alpha = 1;
         this._selectAnim = new Tween(SHOW_SELECT_DURATION,this._selectAnimContainer,{"alpha":0},{"onComplete":this.onSelectAnimComplete});
         this.firstInfoForSelect.hoverEnabled = this.secondInfoForSelect.hoverEnabled = false;
      }
      
      public function togglePartsVisibleAnim(param1:Boolean) : void
      {
         this.clearTweens();
         if(param1)
         {
            this.firstInfoForSelect.x = this._firstItemDefaultX + MODULE_ANIM_OFFSET_X;
            this.firstInfoForSelect.alpha = 0;
            this.secondInfoForSelect.x = this._secondItemDefaultX - MODULE_ANIM_OFFSET_X;
            this.secondInfoForSelect.alpha = 0;
            this.delimiterTF.y = this._delimiterDefaultY;
            this.firstInfoForSelect.y = this.secondInfoForSelect.y = this._moduleDefaultY;
            this.delimiterTF.alpha = 0;
            this._tweens.push(new Tween(SHOW_ANIM_DURATION,this.firstInfoForSelect,{
               "alpha":1,
               "x":this._firstItemDefaultX
            },{
               "ease":Strong.easeOut,
               "delay":SHOW_ANIM_DELAY,
               "onComplete":this.clearTweens
            }));
            this._tweens.push(new Tween(SHOW_ANIM_DURATION,this.secondInfoForSelect,{
               "alpha":1,
               "x":this._secondItemDefaultX
            },{
               "ease":Strong.easeOut,
               "delay":SHOW_ANIM_DELAY
            }));
            this._tweens.push(new Tween(SHOW_ANIM_DURATION,this.delimiterTF,{"alpha":1},{"delay":SHOW_ANIM_DELAY}));
         }
         else
         {
            this._tweens.push(new Tween(HIDE_ANIM_DURATION,this.firstInfoForSelect,{
               "alpha":0,
               "y":this._moduleDefaultY + HIDE_ANIM_ITEMS_OFFSET_Y
            },{
               "ease":Strong.easeOut,
               "onComplete":this.clearTweens
            }));
            this._tweens.push(new Tween(HIDE_ANIM_DURATION,this.secondInfoForSelect,{
               "alpha":0,
               "y":this._moduleDefaultY + HIDE_ANIM_ITEMS_OFFSET_Y
            },{"ease":Strong.easeOut}));
            this._tweens.push(new Tween(HIDE_ANIM_DURATION,this.delimiterTF,{
               "alpha":0,
               "y":this._delimiterDefaultY + HIDE_ANIM_ITEMS_OFFSET_Y
            }));
         }
         this.firstInfoForSelect.hoverEnabled = this.secondInfoForSelect.hoverEnabled = param1;
      }
      
      private function onSelectAnimComplete() : void
      {
         this.clearTweens();
         dispatchEvent(new Event(SELECT_ANIM_COMPLETE));
      }
      
      private function clearSelectAnim() : void
      {
         if(this._selectAnim != null)
         {
            this._selectAnim.dispose();
            this._selectAnim = null;
         }
      }
      
      private function clearTweens() : void
      {
         var _loc1_:Tween = null;
         if(this._tweens.length)
         {
            for each(_loc1_ in this._tweens)
            {
               _loc1_.dispose();
            }
            this._tweens.splice(0,this._tweens.length);
         }
      }
      
      private function updatePosition() : void
      {
         var _loc1_:int = !!this._isBig ? int(MODULE_BIG_OFFSET_X) : int(MODULE_SMALL_OFFSET_X);
         this._firstItemDefaultX = -_loc1_;
         this._secondItemDefaultX = _loc1_;
         this.firstInfoForSelect.x = this._firstItemDefaultX;
         this.secondInfoForSelect.x = this._secondItemDefaultX;
         var _loc2_:int = Math.max(this.firstInfoForSelect.keyViewerPositionY,this.secondInfoForSelect.keyViewerPositionY);
         this.firstInfoForSelect.keyViewerPositionY = _loc2_;
         this.secondInfoForSelect.keyViewerPositionY = _loc2_;
         dispatchEvent(new Event(Event.RESIZE));
      }
   }
}
