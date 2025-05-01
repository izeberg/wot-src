package net.wg.historical_battles.gui.battle.views.spgPanel
{
   import flash.display.Sprite;
   import flash.events.Event;
   import flash.text.TextField;
   import flash.utils.Dictionary;
   import net.wg.data.constants.InvalidationType;
   import net.wg.data.constants.Values;
   import net.wg.historical_battles.gui.battle.views.spgPanel.VO.HBSPGInfoVO;
   import net.wg.historical_battles.gui.battle.views.spgPanel.events.HBSPGPanelEvent;
   import net.wg.historical_battles.infrastructure.base.meta.IHBSPGPanelMeta;
   import net.wg.historical_battles.infrastructure.base.meta.impl.HBSPGPanelMeta;
   import scaleform.clik.motion.Tween;
   
   public class HBSPGPanel extends HBSPGPanelMeta implements IHBSPGPanelMeta
   {
      
      private static const RENDERER_HEIGHT:int = 33;
      
      private static const RENDERER_LINKAGE:String = "HBSPGRendererUI";
      
      private static const TWEEN_SHOW_TIME:int = 300;
       
      
      public var titleTF:TextField = null;
      
      public var container:Sprite = null;
      
      private var _tween:Tween = null;
      
      private var _renderersDict:Dictionary;
      
      private var _vosDict:Dictionary;
      
      private var _spgList:Array = null;
      
      public function HBSPGPanel()
      {
         this._renderersDict = new Dictionary();
         this._vosDict = new Dictionary();
         super();
      }
      
      override protected function setSPGList(param1:Array) : void
      {
         this._spgList = param1;
         invalidateData();
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         App.utils.commons.truncateTextFieldText(this.titleTF,HB_BATTLE.SPGPANEL_TITLE,true,false,Values.THREE_DOTS);
         this.x = -this.width;
      }
      
      override protected function draw() : void
      {
         var _loc1_:HBSPGRenderer = null;
         var _loc2_:HBSPGInfoVO = null;
         var _loc3_:Array = null;
         var _loc4_:int = 0;
         var _loc5_:int = 0;
         var _loc6_:* = null;
         if(!this._spgList)
         {
            return;
         }
         if(isInvalid(InvalidationType.DATA))
         {
            _loc3_ = [];
            _loc4_ = Boolean(this._spgList) ? int(this._spgList.length) : int(0);
            _loc5_ = 0;
            while(_loc5_ < _loc4_)
            {
               _loc2_ = this._vosDict[this._spgList[_loc5_].vehicleID];
               if(_loc2_)
               {
                  _loc2_.update(this._spgList[_loc5_]);
                  _loc1_ = this._renderersDict[_loc2_.vehicleID];
               }
               else
               {
                  _loc2_ = new HBSPGInfoVO(this._spgList[_loc5_]);
                  this._vosDict[_loc2_.vehicleID] = _loc2_;
                  _loc1_ = App.utils.classFactory.getComponent(RENDERER_LINKAGE,HBSPGRenderer);
                  this._renderersDict[_loc2_.vehicleID] = _loc1_;
                  _loc1_.data = _loc2_;
                  this.container.addChild(_loc1_);
               }
               _loc1_.y = _loc5_ * RENDERER_HEIGHT;
               _loc3_[_loc3_.length] = String(_loc2_.vehicleID);
               _loc5_++;
            }
            for(_loc6_ in this._vosDict)
            {
               if(_loc3_.indexOf(_loc6_) == -1)
               {
                  _loc1_ = this._renderersDict[_loc6_];
                  _loc1_.dispose();
                  this.container.removeChild(_loc1_);
                  this._renderersDict[_loc6_] = null;
                  _loc2_ = this._vosDict[_loc6_];
                  _loc2_.dispose();
                  this._vosDict[_loc6_] = null;
               }
            }
            dispatchEvent(new Event(HBSPGPanelEvent.SIZE_CHANGE));
         }
      }
      
      override protected function onDispose() : void
      {
         var _loc1_:HBSPGRenderer = null;
         var _loc2_:HBSPGInfoVO = null;
         var _loc3_:Number = NaN;
         while(this.container.numChildren)
         {
            _loc1_ = this.container.removeChildAt(0) as HBSPGRenderer;
            _loc3_ = _loc1_.vehicleID;
            _loc1_.dispose();
            _loc2_ = this._vosDict[_loc3_];
            _loc2_.dispose();
         }
         App.utils.data.cleanupDynamicObject(this._vosDict);
         this._vosDict = null;
         App.utils.data.cleanupDynamicObject(this._renderersDict);
         this._renderersDict = null;
         this.container = null;
         this.titleTF = null;
         this._spgList = null;
         this.clearTween();
         super.onDispose();
      }
      
      public function as_hideTitle() : void
      {
         this.clearTween();
         this._tween = new Tween(TWEEN_SHOW_TIME,this.titleTF,{"alpha":0});
      }
      
      public function as_setSPGHp(param1:int, param2:int, param3:int) : void
      {
         var _loc4_:HBSPGRenderer = this._renderersDict[param1];
         if(_loc4_)
         {
            _loc4_.setHp(param2,param3);
         }
      }
      
      public function as_show() : void
      {
         this.clearTween();
         this._tween = new Tween(TWEEN_SHOW_TIME,this,{"x":0});
      }
      
      private function clearTween() : void
      {
         if(this._tween)
         {
            this._tween.dispose();
            this._tween = null;
         }
      }
   }
}
