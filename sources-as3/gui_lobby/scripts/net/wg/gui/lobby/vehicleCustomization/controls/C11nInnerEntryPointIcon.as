package net.wg.gui.lobby.vehicleCustomization.controls
{
   import flash.display.FrameLabel;
   import flash.display.MovieClip;
   import flash.geom.Point;
   import net.wg.data.constants.generated.CUSTOMIZATION_ALIASES;
   import net.wg.data.constants.generated.CUSTOMIZATION_CONSTS;
   import net.wg.gui.lobby.vehicleCustomization.data.CustomizationInnerEntryPointVO;
   import net.wg.infrastructure.base.UIComponentEx;
   import net.wg.utils.IScheduler;
   import scaleform.clik.constants.InvalidationType;
   
   public class C11nInnerEntryPointIcon extends UIComponentEx
   {
      
      private static const ICON_ID_EMPTY:String = "empty";
      
      private static const SMALL_PREFIX:String = "small_";
      
      private static const ANIM_DELAY:int = 5000;
       
      
      private var _frameKey:String = "empty";
      
      private var _allowedFrames:Vector.<String> = null;
      
      private var _allowedIcons:Vector.<String>;
      
      private var _data:CustomizationInnerEntryPointVO = null;
      
      private var _currentAnimID:String = "";
      
      private var _currentAnim:MovieClip = null;
      
      private var _frameIDToAnimLinkageMap:Object = null;
      
      private var _sheduler:IScheduler;
      
      public function C11nInnerEntryPointIcon()
      {
         this._allowedIcons = new <String>[CUSTOMIZATION_CONSTS.INNER_ENTRY_POINT_PROGRESSIVE,CUSTOMIZATION_CONSTS.INNER_ENTRY_POINT_STATS_TRACKER];
         this._sheduler = App.utils.scheduler;
         super();
         this._frameIDToAnimLinkageMap = new Object();
         this._frameIDToAnimLinkageMap[CUSTOMIZATION_CONSTS.INNER_ENTRY_POINT_STATS_TRACKER] = new AnimProps(CUSTOMIZATION_ALIASES.INNER_ENTRY_POINT_STATS_TRACKER_ANIM,new Point(30,10));
         this._frameIDToAnimLinkageMap[SMALL_PREFIX + CUSTOMIZATION_CONSTS.INNER_ENTRY_POINT_STATS_TRACKER] = new AnimProps(CUSTOMIZATION_ALIASES.INNER_ENTRY_POINT_STATS_TRACKER_ANIM,new Point(0,0));
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this._allowedFrames = new Vector.<String>(0);
         var _loc1_:Array = currentLabels;
         var _loc2_:int = _loc1_.length;
         var _loc3_:FrameLabel = null;
         var _loc4_:uint = 0;
         while(_loc4_ < _loc2_)
         {
            _loc3_ = _loc1_[_loc4_];
            this._allowedFrames.push(_loc3_.name);
            _loc4_++;
         }
      }
      
      override protected function onDispose() : void
      {
         var _loc1_:* = undefined;
         stop();
         this.removeAnim();
         this._data = null;
         this._allowedIcons.length = 0;
         this._allowedIcons = null;
         if(this._allowedFrames != null)
         {
            this._allowedFrames.splice(0,this._allowedFrames.length);
            this._allowedFrames = null;
         }
         for(_loc1_ in this._frameIDToAnimLinkageMap)
         {
            this._frameIDToAnimLinkageMap[_loc1_] = null;
            delete this._frameIDToAnimLinkageMap[_loc1_];
         }
         this._frameIDToAnimLinkageMap = null;
         this._sheduler = null;
         super.onDispose();
      }
      
      override protected function draw() : void
      {
         super.draw();
         if(this._data == null)
         {
            return;
         }
         if(isInvalid(InvalidationType.DATA))
         {
            this.updateData();
         }
      }
      
      public function setData(param1:CustomizationInnerEntryPointVO) : void
      {
         this._data = param1;
         invalidateData();
      }
      
      private function updateData() : void
      {
         var _loc1_:String = !!this._data.isSmall ? SMALL_PREFIX + this._data.itemId : this._data.itemId;
         if(this._frameKey != _loc1_)
         {
            this._frameKey = _loc1_;
            gotoAndStop(_loc1_);
         }
         if(this._data.hasNovelty)
         {
            if(this._currentAnimID != this._frameKey)
            {
               this.addAnim();
            }
         }
         else
         {
            this.removeAnim();
         }
         invalidateState();
      }
      
      private function addAnim() : void
      {
         var _loc1_:AnimProps = null;
         this.removeAnim();
         if(this._frameIDToAnimLinkageMap.hasOwnProperty(this._frameKey))
         {
            _loc1_ = this._frameIDToAnimLinkageMap[this._frameKey];
            this._currentAnim = App.utils.classFactory.getComponent(_loc1_.linkage,MovieClip);
            this._currentAnim.x = _loc1_.position.x;
            this._currentAnim.y = _loc1_.position.y;
            App.utils.commons.setBlur(this._currentAnim,4,4);
            this._currentAnimID = this._frameKey;
            this.addChild(this._currentAnim);
            this.runAnim();
         }
      }
      
      private function removeAnim() : void
      {
         if(this._currentAnim != null)
         {
            this.stopAnim();
            this._currentAnim.stop();
            this.removeChild(this._currentAnim);
            this._currentAnim = null;
            this._currentAnimID = null;
         }
      }
      
      private function runAnim() : void
      {
         if(this._currentAnim != null)
         {
            this._currentAnim.play();
            this._sheduler.scheduleTask(this.runAnim,ANIM_DELAY);
         }
      }
      
      private function stopAnim() : void
      {
         this._sheduler.cancelTask(this.runAnim);
      }
   }
}

import flash.geom.Point;

class AnimProps
{
    
   
   private var _linkage:String = "";
   
   private var _position:Point = null;
   
   function AnimProps(param1:String, param2:Point)
   {
      super();
      this._linkage = param1;
      this._position = param2;
   }
   
   public function get linkage() : String
   {
      return this._linkage;
   }
   
   public function get position() : Point
   {
      return this._position;
   }
}
