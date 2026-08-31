package net.wg.gui.battle.views.minimap
{
   import flash.display.DisplayObject;
   import flash.display.DisplayObjectContainer;
   import flash.events.TimerEvent;
   import flash.utils.Dictionary;
   import flash.utils.Timer;
   import net.wg.data.constants.Errors;
   import net.wg.gui.battle.views.minimap.components.entries.interfaces.IMinimapEntryWithNonScaleContent;
   import net.wg.gui.battle.views.minimap.components.entries.interfaces.IVehicleMinimapEntry;
   import net.wg.gui.battle.views.minimap.components.entries.vehicle.MinimapEntryLabelHelper;
   import net.wg.gui.battle.views.minimap.constants.MinimapSizeConst;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   import net.wg.utils.IAssertable;
   
   public class MinimapEntryController implements IDisposable
   {
      
      private static var _instance:MinimapEntryController = null;
      
      private static const LABEL_TICK_INTERVAL:int = 330;
       
      
      private var _vehicleEntries:Vector.<IVehicleMinimapEntry>;
      
      private var _vehicleLabelsEntries:Vector.<IVehicleMinimapEntry>;
      
      private var _isDisposed:Boolean = false;
      
      private var _asserter:IAssertable;
      
      private var _highlightedEntries:Vector.<IVehicleMinimapEntry>;
      
      private var _isShowVehicleNamesTurnedOn:Boolean = false;
      
      private var _scalableEntries:Vector.<DisplayObject>;
      
      private var _scalableEntriesWithNonScaleContent:Vector.<IMinimapEntryWithNonScaleContent>;
      
      private var _nonScalableEntries:Vector.<DisplayObject>;
      
      private var _sizeIndexByContainer:Dictionary;
      
      private var _labelTimer:Timer;
      
      private var _activeLabelHelpers:Vector.<MinimapEntryLabelHelper>;
      
      public function MinimapEntryController()
      {
         this._vehicleEntries = new Vector.<IVehicleMinimapEntry>();
         this._vehicleLabelsEntries = new Vector.<IVehicleMinimapEntry>();
         this._asserter = App.utils.asserter;
         this._highlightedEntries = new Vector.<IVehicleMinimapEntry>(0);
         this._scalableEntries = new Vector.<DisplayObject>();
         this._scalableEntriesWithNonScaleContent = new Vector.<IMinimapEntryWithNonScaleContent>();
         this._nonScalableEntries = new Vector.<DisplayObject>();
         this._sizeIndexByContainer = new Dictionary();
         this._activeLabelHelpers = new Vector.<MinimapEntryLabelHelper>();
         super();
         if(_instance)
         {
            App.utils.asserter.assertNotNull(_instance,"MinimapEntryController singleton... use get instance()");
         }
         _instance = this;
         this._labelTimer = new Timer(LABEL_TICK_INTERVAL);
         this._labelTimer.addEventListener(TimerEvent.TIMER,this.onLabelTimerHandler,false,0,true);
      }
      
      public static function get instance() : MinimapEntryController
      {
         if(_instance == null)
         {
            _instance = new MinimapEntryController();
         }
         return _instance;
      }
      
      public final function dispose() : void
      {
         this.verifyIsDisposed();
         this._isDisposed = true;
         this._asserter = null;
         PendingEntryData.clear();
         this._scalableEntries.splice(0,this._scalableEntries.length);
         this._scalableEntries = null;
         this._scalableEntriesWithNonScaleContent.splice(0,this._scalableEntriesWithNonScaleContent.length);
         this._scalableEntriesWithNonScaleContent = null;
         this._vehicleEntries.splice(0,this._vehicleEntries.length);
         this._vehicleEntries = null;
         this._vehicleLabelsEntries.splice(0,this._vehicleLabelsEntries.length);
         this._vehicleLabelsEntries = null;
         this._nonScalableEntries.length = 0;
         this._nonScalableEntries = null;
         this._highlightedEntries.length = 0;
         this._highlightedEntries = null;
         this._labelTimer.removeEventListener(TimerEvent.TIMER,this.onLabelTimerHandler);
         this._labelTimer.stop();
         this._labelTimer = null;
         this._activeLabelHelpers.length = 0;
         this._activeLabelHelpers = null;
         App.utils.data.cleanupDynamicObject(this._sizeIndexByContainer);
         this._sizeIndexByContainer = null;
      }
      
      public function hideVehiclesName() : void
      {
         var _loc1_:IVehicleMinimapEntry = null;
         this._isShowVehicleNamesTurnedOn = false;
         for each(_loc1_ in this._vehicleLabelsEntries)
         {
            _loc1_.hideVehicleName();
         }
      }
      
      public function highlight(param1:Number) : void
      {
         var _loc2_:IVehicleMinimapEntry = null;
         this._highlightedEntries.length = 0;
         for each(_loc2_ in this._vehicleEntries)
         {
            if(_loc2_.vehicleID == param1)
            {
               this._highlightedEntries.push(_loc2_);
               _loc2_.highlight();
            }
         }
      }
      
      public function isDisposed() : Boolean
      {
         return this._isDisposed;
      }
      
      public function registerActiveLabelHelper(param1:MinimapEntryLabelHelper) : void
      {
         if(this._activeLabelHelpers.indexOf(param1) == -1)
         {
            this._activeLabelHelpers.push(param1);
            if(!this._labelTimer.running)
            {
               this._labelTimer.start();
            }
         }
      }
      
      public function registerNonScalableEntry(param1:DisplayObject) : void
      {
         if(param1.stage == null)
         {
            PendingEntryData.create(param1,PendingEntryData.NON_SCALABLE);
            return;
         }
         this._nonScalableEntries.push(param1);
         param1.scaleX = param1.scaleY = MinimapSizeConst.ENTRY_CONTR_SCALES[this.getSizeIndex(param1)];
      }
      
      public function registerScalableEntry(param1:DisplayObject, param2:Boolean = false) : void
      {
         if(param1.stage == null)
         {
            PendingEntryData.create(param1,!!param2 ? int(PendingEntryData.SCALABLE_WITH_NON_SCALABLE_CONTENT) : int(PendingEntryData.SCALABLE));
            return;
         }
         this._scalableEntries.push(param1);
         var _loc3_:int = this.getSizeIndex(param1);
         var _loc4_:Number = MinimapSizeConst.ENTRY_SCALES[_loc3_];
         if(_loc4_ != param1.scaleX)
         {
            param1.scaleX = param1.scaleY = _loc4_;
         }
         if(param2)
         {
            this._scalableEntriesWithNonScaleContent.push(IMinimapEntryWithNonScaleContent(param1));
            IMinimapEntryWithNonScaleContent(param1).setContentNormalizedScale(MinimapSizeConst.ENTRY_INTERNAL_CONTENT_CONTR_SCALES[_loc3_]);
         }
      }
      
      public function registerVehicleEntry(param1:IVehicleMinimapEntry) : void
      {
         this.verifyIsDisposed();
         if(this._vehicleEntries.indexOf(param1) == -1)
         {
            this._vehicleEntries.push(param1);
         }
         if(this._highlightedEntries.length != 0 && this._highlightedEntries[0].vehicleID == param1.vehicleID)
         {
            this._highlightedEntries.push(param1);
            param1.highlight();
         }
      }
      
      public function registerVehicleLabelEntry(param1:IVehicleMinimapEntry) : void
      {
         var _loc2_:DisplayObject = param1 as DisplayObject;
         if(_loc2_.stage == null)
         {
            PendingEntryData.create(_loc2_,PendingEntryData.NON_SCALABLE);
            return;
         }
         this.verifyIsDisposed();
         if(this._vehicleLabelsEntries.indexOf(param1) == -1)
         {
            this._vehicleLabelsEntries.push(param1);
            param1.updateSizeIndex(this.getSizeIndex(_loc2_));
         }
         if(this._isShowVehicleNamesTurnedOn)
         {
            param1.showVehicleName();
         }
         else
         {
            param1.hideVehicleName();
         }
      }
      
      public function showVehiclesName() : void
      {
         var _loc1_:IVehicleMinimapEntry = null;
         this._isShowVehicleNamesTurnedOn = true;
         for each(_loc1_ in this._vehicleLabelsEntries)
         {
            _loc1_.showVehicleName();
         }
      }
      
      public function unhighlight() : void
      {
         var _loc1_:IVehicleMinimapEntry = null;
         for each(_loc1_ in this._highlightedEntries)
         {
            _loc1_.unhighlight();
         }
         this._highlightedEntries.length = 0;
      }
      
      public function unregisterActiveLabelHelper(param1:MinimapEntryLabelHelper) : void
      {
         var _loc2_:int = this._activeLabelHelpers.indexOf(param1);
         if(_loc2_ != -1)
         {
            this._activeLabelHelpers.splice(_loc2_,1);
            if(this._activeLabelHelpers.length == 0)
            {
               this._labelTimer.stop();
            }
         }
      }
      
      public function unregisterNonScalableEntry(param1:DisplayObject) : void
      {
         var _loc2_:int = this._nonScalableEntries.indexOf(param1);
         if(_loc2_ != -1)
         {
            this._nonScalableEntries.splice(_loc2_,1);
         }
      }
      
      public function unregisterScalableEntry(param1:DisplayObject, param2:Boolean = false) : void
      {
         var _loc3_:int = this._scalableEntries.indexOf(param1);
         if(_loc3_ != -1)
         {
            this._scalableEntries.splice(_loc3_,1);
         }
         if(param2)
         {
            _loc3_ = this._scalableEntriesWithNonScaleContent.indexOf(param1);
            if(_loc3_ != -1)
            {
               this._scalableEntriesWithNonScaleContent.splice(_loc3_,1);
            }
         }
      }
      
      public function unregisterVehicleEntry(param1:IVehicleMinimapEntry) : void
      {
         this.verifyIsDisposed();
         var _loc2_:int = this._vehicleEntries.indexOf(param1);
         if(_loc2_ != -1)
         {
            this._vehicleEntries.splice(_loc2_,1);
         }
      }
      
      public function unregisterVehicleLabelEntry(param1:IVehicleMinimapEntry) : void
      {
         this.verifyIsDisposed();
         var _loc2_:int = this._vehicleLabelsEntries.indexOf(param1);
         if(_loc2_ != -1)
         {
            this._vehicleLabelsEntries.splice(_loc2_,1);
         }
      }
      
      public function updateScale(param1:int, param2:DisplayObjectContainer) : void
      {
         var _loc4_:* = undefined;
         var _loc5_:DisplayObject = null;
         var _loc6_:Number = NaN;
         var _loc7_:Boolean = false;
         var _loc8_:IMinimapEntryWithNonScaleContent = null;
         var _loc9_:IVehicleMinimapEntry = null;
         this._sizeIndexByContainer[param2] = param1;
         var _loc3_:int = 0;
         for(_loc4_ in this._sizeIndexByContainer)
         {
            _loc3_++;
            if(_loc3_ > 1)
            {
               break;
            }
         }
         _loc5_ = null;
         _loc6_ = MinimapSizeConst.ENTRY_SCALES[param1];
         _loc7_ = _loc3_ == 1;
         for each(_loc5_ in this._scalableEntries)
         {
            if(_loc7_ || param2.contains(_loc5_))
            {
               if(_loc6_ != _loc5_.scaleX)
               {
                  _loc5_.scaleX = _loc5_.scaleY = _loc6_;
               }
            }
         }
         _loc6_ = MinimapSizeConst.ENTRY_CONTR_SCALES[param1];
         for each(_loc5_ in this._nonScalableEntries)
         {
            if(_loc7_ || param2.contains(_loc5_))
            {
               _loc5_.scaleX = _loc5_.scaleY = _loc6_;
            }
         }
         _loc8_ = null;
         for each(_loc8_ in this._scalableEntriesWithNonScaleContent)
         {
            if(_loc7_ || param2.contains(_loc8_ as DisplayObject))
            {
               _loc8_.setContentNormalizedScale(MinimapSizeConst.ENTRY_INTERNAL_CONTENT_CONTR_SCALES[param1]);
            }
         }
         for each(_loc9_ in this._vehicleLabelsEntries)
         {
            if(_loc7_ || param2.contains(_loc9_ as DisplayObject))
            {
               _loc9_.updateSizeIndex(param1);
            }
         }
      }
      
      private function verifyIsDisposed() : void
      {
         this._asserter.assert(!this._isDisposed,"MinimapEntryController " + Errors.ALREADY_DISPOSED);
      }
      
      private function getSizeIndex(param1:DisplayObject) : int
      {
         var _loc2_:DisplayObjectContainer = param1.parent;
         while(_loc2_ != null)
         {
            if(_loc2_ in this._sizeIndexByContainer)
            {
               return this._sizeIndexByContainer[_loc2_];
            }
            _loc2_ = _loc2_.parent;
         }
         return MinimapSizeConst.MIN_SIZE_INDEX;
      }
      
      public function get isShowVehicleNamesTurnedOn() : Boolean
      {
         return this._isShowVehicleNamesTurnedOn;
      }
      
      private function onLabelTimerHandler(param1:TimerEvent) : void
      {
         var _loc2_:MinimapEntryLabelHelper = null;
         for each(_loc2_ in this._activeLabelHelpers)
         {
            _loc2_.timerUpdate();
         }
      }
   }
}

import flash.display.DisplayObject;
import flash.events.Event;
import net.wg.gui.battle.views.minimap.MinimapEntryController;
import net.wg.gui.battle.views.minimap.components.entries.interfaces.IVehicleMinimapEntry;

class PendingEntryData
{
   
   private static var _pendingItems:Vector.<PendingEntryData> = new Vector.<PendingEntryData>(0);
   
   public static const NON_SCALABLE:int = 0;
   
   public static const SCALABLE:int = 1;
   
   public static const SCALABLE_WITH_NON_SCALABLE_CONTENT:int = 3;
   
   public static const VEHICLE_LABEL:int = 4;
    
   
   private var _entry:DisplayObject;
   
   private var _kind:int;
   
   function PendingEntryData(param1:DisplayObject, param2:int)
   {
      super();
      this._entry = param1;
      this._kind = param2;
      this._entry.addEventListener(Event.ADDED_TO_STAGE,this.addedToStageHandler);
   }
   
   public static function create(param1:DisplayObject, param2:int) : void
   {
      _pendingItems.push(new PendingEntryData(param1,param2));
   }
   
   public static function clear() : void
   {
      var _loc1_:PendingEntryData = null;
      for each(_loc1_ in _pendingItems)
      {
         _loc1_.dispose();
      }
      _pendingItems.length = 0;
   }
   
   public function dispose() : void
   {
      this._entry.removeEventListener(Event.ADDED_TO_STAGE,this.addedToStageHandler);
      this._entry = null;
   }
   
   private function addedToStageHandler(param1:Event) : void
   {
      this._entry.removeEventListener(Event.ADDED_TO_STAGE,this.addedToStageHandler);
      var _loc2_:int = _pendingItems.indexOf(this);
      if(_loc2_ != -1)
      {
         _pendingItems.splice(_loc2_,1);
      }
      switch(this._kind)
      {
         case NON_SCALABLE:
            MinimapEntryController.instance.registerNonScalableEntry(this._entry);
            break;
         case SCALABLE:
            MinimapEntryController.instance.registerScalableEntry(this._entry);
            break;
         case SCALABLE_WITH_NON_SCALABLE_CONTENT:
            MinimapEntryController.instance.registerScalableEntry(this._entry,true);
            break;
         case VEHICLE_LABEL:
            MinimapEntryController.instance.registerVehicleLabelEntry(this._entry as IVehicleMinimapEntry);
      }
   }
}
